import json
from datetime import datetime
from http import HTTPStatus

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from app.constants.loans_constants import wrong_payment_error
from app.forms.loans_forms import CanUserLoanForm, ReturnLoanForm
from app.models import Reservation
from app.services.customer_svc import customer_exists
from app.services.loans_svc import can_customer_loan, get_fine, get_loan, serialize_loan


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

    customer = customer_exists(form.customer_id)

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
