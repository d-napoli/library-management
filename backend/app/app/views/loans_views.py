import json
from datetime import date, datetime
from http import HTTPStatus

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from app.constants.customers_constants import customer_cant_loan_error, customer_not_found_error
from app.constants.exemplaries_constants import no_available_exemplaries_found
from app.constants.loans_constants import wrong_payment_error, wrong_start_end_dates_error
from app.forms.loans_forms import CanUserLoanForm, NewLoanForm, ReturnLoanForm
from app.models import Reservation
from app.services.customer_svc import can_customer_loan, return_customer_if_exists
from app.services.exemplaries_svc import (
    get_available_exemplary_based_on_work,
    is_exemplary_borrowed,
    return_exemplary_if_exists,
)
from app.services.loans_svc import dates_valid, get_fine, get_loan, serialize_loan
from app.services.work_svc import get_work_if_exists


@csrf_exempt
@require_GET
def list_all_loans(request):
    loans = Reservation.objects.all().order_by("-end_date")

    data = json.dumps([serialize_loan(l) for l in loans])
    return JsonResponse({"loans": json.loads(data)}, status=HTTPStatus.ACCEPTED)


@csrf_exempt
@require_GET
def can_customer_loans(request):
    form = CanUserLoanForm.parse_raw(request.body)

    customer = return_customer_if_exists(form.customer_id)

    if not customer:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)

    return JsonResponse({"user_id": customer.id, "can_loan": can_customer_loan(customer)})


@csrf_exempt
@require_POST
def return_loan(request):
    form = ReturnLoanForm.parse_raw(request.body)

    loan_found, loan = get_loan(form.loan_id)

    if not loan_found:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)

    if loan.return_date:
        return JsonResponse({"message": "Retorno já realizado"}, status=HTTPStatus.CONFLICT)

    payment_amount = form.payment_amount
    expected_fine = get_fine(loan.end_date)

    payment_amount = 0 if not payment_amount else payment_amount

    if expected_fine > 0 and payment_amount < expected_fine:
        return JsonResponse(
            {"message": wrong_payment_error(payment_amount, expected_fine)}, status=HTTPStatus.BAD_REQUEST
        )

    loan.return_date = datetime.now()
    loan.save()

    return JsonResponse({}, status=HTTPStatus.ACCEPTED)


@csrf_exempt
@require_POST
def new_loan(request):
    form = NewLoanForm.parse_raw(request.body)

    start_date = datetime.strptime(form.start_date, "%Y-%m-%d")
    end_date = datetime.strptime(form.end_date, "%Y-%m-%d")

    if not dates_valid(start_date, end_date):
        return JsonResponse({"message": wrong_start_end_dates_error()}, status=HTTPStatus.BAD_REQUEST)

    work = get_work_if_exists(form.work_id)

    if not work:
        return JsonResponse({"message": "Work not found"}, status=HTTPStatus.NOT_FOUND)

    exemplary = get_available_exemplary_based_on_work(work)

    if not exemplary:
        return JsonResponse({"message": no_available_exemplaries_found()}, status=HTTPStatus.NOT_FOUND)

    # Validate customer
    customer = return_customer_if_exists(form.customer_id)

    if not customer:
        return JsonResponse({"message": customer_not_found_error(form.customer_id)}, status=HTTPStatus.NOT_FOUND)

    if not can_customer_loan(customer):
        return JsonResponse({"message": customer_cant_loan_error(customer)}, status=HTTPStatus.BAD_REQUEST)

    r = Reservation(start_date=start_date, end_date=end_date, reserved_customer=customer, exemplary=exemplary)
    r.save()

    return JsonResponse({}, status=HTTPStatus.ACCEPTED)
