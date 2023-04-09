from app.models import Exemplary, Reservation


def serialize_exemplary(exemplary: Exemplary):
    return {
        "id": exemplary.pk,
        "title": exemplary.work.title,
        "author": exemplary.work.author.name,
        "type": exemplary.work.type,
        "is_borrowed": is_exemplary_borrowed(exemplary),
        "active": exemplary.is_active,
    }


def is_exemplary_borrowed(exemplary):
    loans = Reservation.objects.filter(exemplary=exemplary, return_date=None)
    return bool(loans)
