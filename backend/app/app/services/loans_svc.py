from datetime import datetime

from app.constants.loans_constants import get_fine_per_day
from app.models import Reservation
from app.services.customer_svc import serialize_customer
from app.services.exemplaries_svc import serialize_exemplary


def serialize_loan(loan: Reservation):
    return {
        "id": loan.pk,
        "start_date": str(loan.start_date),
        "end_date": str(loan.end_date),
        "return_date": get_return_date(loan),
        "is_devolution_late": is_devolution_late(loan),
        "fine_per_day": get_fine_per_day(),
        "days_late": get_days_late(loan.end_date),
        "fine": get_fine(loan.end_date),
        "customer": serialize_customer(loan.reserved_customer),
        "exemplary": serialize_exemplary(loan.exemplary),
    }


def is_devolution_late(loan):
    if bool(loan.return_date):
        return False

    return datetime.now().date() > loan.end_date


def get_return_date(loan):
    return None if not loan.return_date else str(loan.return_date)


def get_days_late(end_date):
    today = datetime.now().date()

    if today < end_date:
        return 0

    return (today - end_date).days


def get_fine(end_date) -> int:
    return get_days_late(end_date) * get_fine_per_day()


def get_loan(loan_id):
    loan = Reservation.objects.filter(pk=loan_id).first()

    return bool(loan), loan


def dates_valid(start_date, end_date):
    today = datetime.now().date()

    if start_date.date() >= end_date.date():
        return False

    if start_date.date() < today or end_date.date() < today:
        return False

    return True
