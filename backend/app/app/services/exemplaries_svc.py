from app.models import Exemplary, Reservation, Work


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


def return_exemplary_if_exists(exemplary_id, only_search_actives=True):
    exemplary = Exemplary.objects.filter(pk=exemplary_id)

    if only_search_actives:
        exemplary.filter(is_active=True)

    return exemplary.first()


def get_available_exemplary_based_on_work(work: Work):
    exemplaries = Exemplary.objects.filter(work=work)

    for exemplary in exemplaries:
        if exemplary.is_active and not is_exemplary_borrowed(exemplary):
            return exemplary

    return None
