from app.models import Customer, Reservation


def serialize_customer(customer: Customer) -> dict:
    return {
        "id": customer.id,
        "first_name": customer.first_name,
        "last_name": customer.last_name,
        "email": customer.email,
        "type": customer.user_type,
        "is_active": customer.is_active,
    }


def return_customer_if_exists(id: int) -> bool:
    customer = Customer.objects.filter(pk=id).first()

    return customer


def customer_already_exists(email: str) -> bool:
    customer = Customer.objects.filter(email=email)

    return len(customer) > 0


def can_customer_loan(customer):
    customer_has_open_loans = bool(Reservation.objects.filter(reserved_customer=customer))
    can_loan = not customer_has_open_loans and customer.is_active

    return can_loan


def is_customer_teacher(customer):
    return customer.user_type == Customer.CustomerType.TEACHER
