import json
from http import HTTPStatus

from app.constants.authors_constants import author_exists_error, author_not_found_error
from app.forms.authors_forms import BaseAuthorForm
from app.models import Author
from app.services.authors_svc import author_exists, author_name_taken, serialize_author
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@csrf_exempt
@require_POST
def add_author(request):
    form = BaseAuthorForm.parse_raw(request.body)

    if author_name_taken(form.name):
        return JsonResponse({"message": author_exists_error()}, status=HTTPStatus.CONFLICT)

    author = Author(name=form.name)
    author.save()

    response_body = serialize_author(author)
    return JsonResponse(response_body, status=HTTPStatus.CREATED)


@csrf_exempt
@require_http_methods(["PATCH"])
def edit_author(request, author_id):
    form = BaseAuthorForm.parse_raw(request.body)

    if not author_exists(author_id):
        return JsonResponse({"message": author_not_found_error()}, status=HTTPStatus.NOT_FOUND)

    if author_name_taken(form.name):
        return JsonResponse({"message": author_exists_error(form.name)}, status=HTTPStatus.CONFLICT)

    author = Author.objects.get(pk=author_id)
    author.name = form.name
    author.save()

    response_body = serialize_author(author)
    return JsonResponse(response_body, status=HTTPStatus.ACCEPTED)


@csrf_exempt
@require_GET
def list_all_authors(request):
    all_authors = Author.objects.all().order_by("pk")
    data = json.dumps([serialize_author(c) for c in all_authors])
    return JsonResponse({"authors": json.loads(data)})
