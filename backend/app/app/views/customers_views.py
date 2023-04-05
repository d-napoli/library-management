import json
from http import HTTPStatus

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods

from app.forms.customer_forms import UpdateCustomerForm
from app.models import Customer


@require_GET
def list_all_customers(request):
    all_customers = Customer.objects.filter(is_active=True).order_by("pk")
    data = json.dumps(
        [{"id": c.pk, "first_name": c.first_name, "last_name": c.last_name, "email": c.email} for c in all_customers]
    )
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
    customer = Customer.objects.filter(pk=int(customer_id), is_active=False).first()

    if customer:
        customer.is_active = True
        customer.save()

        return_data = {}
        status_code = HTTPStatus.ACCEPTED
    else:
        return_data = {"message": f"User with id '{customer_id}' not found"}
        status_code = HTTPStatus.NOT_FOUND

    return JsonResponse(return_data, status=status_code)


@csrf_exempt
@require_GET
def search_customer(request, customer_id):
    try:
        customer = Customer.objects.filter(pk=int(customer_id), is_active=True).get()

        return_data = {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
        }
        status_code = HTTPStatus.ACCEPTED
    except Customer.DoesNotExist:
        return_data = {"message": f"User with id '{customer_id}' not found"}
        status_code = HTTPStatus.NOT_FOUND

    return JsonResponse(return_data, status=status_code)


@csrf_exempt
@require_http_methods(["PATCH"])
def update_customer_info(request, customer_id):
    form = UpdateCustomerForm.parse_raw(request.body)

    customer = Customer.objects.filter(pk=customer_id, is_active=True).first()

    return_data = {"message": f"User with id '{customer_id}' not found"}
    status_code = HTTPStatus.NOT_FOUND

    if customer:
        customer.first_name = form.first_name if form.first_name else customer.first_name
        customer.last_name = form.last_name if form.last_name else customer.last_name
        customer.email = form.email if form.email else customer.email

        customer.save()

        return_data = {
            "id": customer_id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "email": customer.email,
        }
        status_code = HTTPStatus.ACCEPTED

    return JsonResponse(return_data, status=status_code)
