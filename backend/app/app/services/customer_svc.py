from app.models import Customer


def serialize_customer(customer: Customer) -> dict:
    return {
        "id": customer.id,
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
    }


def customer_already_exists(email: str) -> bool:
    customer = Customer.objects.filter(email=email)

    return len(customer) > 0
