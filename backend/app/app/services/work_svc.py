from django.db.models import Count

from app.models import Work


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
