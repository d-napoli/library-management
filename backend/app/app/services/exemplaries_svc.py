from app.models import Exemplary


def serialize_exemplary(exemplary: Exemplary):
    return {
        "id": exemplary.pk,
        "title": exemplary.work.title,
        "author": exemplary.work.author.name,
        "type": exemplary.work.type,
    }
