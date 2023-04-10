from django.db.models import Count

from app.models import Exemplary, Reservation, Work


def serialize_work(work_id: int) -> dict:
    work = Work.objects.filter(pk=work_id).annotate(count=Count("work_rel")).first()
    return {"id": work.pk, "title": work.title, "author": work.author.name, "type": work.type, "quantity": work.count}


def work_exists(title: str, author_name: str) -> bool:
    work = Work.objects.filter(title=title, author__name=author_name)
    return len(work) > 0


def get_work_if_exists(work_id):
    try:
        return Work.objects.get(pk=work_id)
    except Work.DoesNotExist:
        return False


def get_teachers_name_who_blocked_loan(work):
    if not work.special_teacher_loan:
        return None

    return f"{work.teacher_reserved.first_name} {work.teacher_reserved.last_name}"


def is_work_blocked_to_loan(work):
    reservation = Reservation.objects.filter(
        exemplary__work=work, return_date__isnull=True, exemplary__work__special_teacher_loan=True
    )

    return len(reservation) > 0
