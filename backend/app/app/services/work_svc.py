from app.models import Author, Work


def serialize_work(work: Work) -> dict:
    return {
        "id": work.pk,
        "title": work.title,
        "author": work.author.name,
        "type": work.type,
    }


def work_exists(title: str, author_name: str) -> bool:
    work = Work.objects.filter(title=title, author__name=author_name)
    return len(work) > 0
