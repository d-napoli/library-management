from app.models import Author


def author_name_taken(author_name) -> bool:
    author = Author.objects.filter(name=author_name)

    return len(author) > 0


def author_exists(id) -> bool:
    try:
        Author.objects.get(pk=id)
        return True
    except Author.DoesNotExist:
        return False


def serialize_author(author: Author) -> dict:
    return {"id": author.pk, "name": author.name}
