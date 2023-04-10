import json
from http import HTTPStatus

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from app.constants.customers_constants import customer_exists_error, customer_not_found_error
from app.forms.customer_forms import AddCustomerForm, UpdateCustomerForm
from app.models import Customer
from app.services.customer_svc import customer_already_exists, serialize_customer


@csrf_exempt
@require_GET
def list_all_customers(request):
    all_customers = Customer.objects.filter().order_by("pk")
    data = json.dumps([serialize_customer(c) for c in all_customers])
    return JsonResponse({"customers": json.loads(data)})


@csrf_exempt
@require_http_methods(["DELETE"])
def soft_delete_customer(request, customer_id):
    customer = Customer.objects.filter(pk=int(customer_id), is_active=True).first()

    if customer:
        customer.is_active = False
        customer.save()

        return_data = {}
        status_code = HTTPStatus.ACCEPTED
    else:
        return_data = {"message": f"User with id '{customer_id}' not found"}
        status_code = HTTPStatus.NOT_FOUND

    return JsonResponse(return_data, status=status_code)


@csrf_exempt
@require_http_methods(["PATCH"])
def reactivate_customer(request, customer_id):
    customer_id = int(customer_id)

    customer = Customer.objects.filter(pk=customer_id, is_active=False).first()

    if customer:
        customer.is_active = True
        customer.save()

        return_data = {}
        status_code = HTTPStatus.ACCEPTED
    else:
        return_data = {"message": customer_not_found_error(customer_id)}
        status_code = HTTPStatus.NOT_FOUND

    return JsonResponse(return_data, status=status_code)


@csrf_exempt
@require_GET
def search_customer(request, customer_id):
    try:
        customer = Customer.objects.filter(pk=int(customer_id), is_active=True).get()

        return_data = serialize_customer(customer)
        status_code = HTTPStatus.ACCEPTED
    except Customer.DoesNotExist:
        return_data = {"message": customer_not_found_error(customer_id)}
        status_code = HTTPStatus.NOT_FOUND

    return JsonResponse(return_data, status=status_code)


@csrf_exempt
@require_http_methods(["PATCH"])
def update_customer_info(request, customer_id):
    form = UpdateCustomerForm.parse_raw(request.body)

    customer = Customer.objects.filter(pk=customer_id, is_active=True).first()

    return_data = {"message": customer_not_found_error(customer_id)}
    status_code = HTTPStatus.NOT_FOUND

    if customer:
        customer.first_name = form.first_name if form.first_name else customer.first_name
        customer.last_name = form.last_name if form.last_name else customer.last_name
        customer.user_type = form.user_type if form.user_type else customer.user_type

        if form.email and customer_already_exists(form.email):
            return JsonResponse({"message": customer_exists_error(form.email)}, status=HTTPStatus.CONFLICT)

        customer.email = form.email if form.email else customer.email

        customer.save()

        return_data = serialize_customer(customer)
        status_code = HTTPStatus.ACCEPTED

    return JsonResponse(return_data, status=status_code)


@csrf_exempt
@require_POST
def add_a_customer(request):
    form = AddCustomerForm.parse_raw(request.body)

    if customer_already_exists(form.email):
        return JsonResponse(
            {"message": customer_exists_error(form.email)},
            status=HTTPStatus.CONFLICT,
        )

    c = Customer(first_name=form.first_name, last_name=form.last_name, email=form.email)
    c.save()

    response_body = serialize_customer(c)

    return JsonResponse(response_body, status=HTTPStatus.ACCEPTED)
