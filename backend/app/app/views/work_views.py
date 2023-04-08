import json
from http import HTTPStatus

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from app.constants.work_constants import work_already_exists_error, work_not_found_error
from app.forms.work_forms import AddWorkForm, UpdateWorkForm
from app.models import Author, Work
from app.services.work_svc import serialize_work, work_exists


@csrf_exempt
@require_GET
def list_all_works(request):
    all_works = Work.objects.all().order_by("pk")
    data = json.dumps([serialize_work(w.pk) for w in all_works])
    return JsonResponse({"works": json.loads(data)}, status=HTTPStatus.ACCEPTED)


@csrf_exempt
@require_POST
def add_work(request):
    form = AddWorkForm.parse_raw(request.body)

    if work_exists(form.title, form.author_name):
        return JsonResponse({"message": work_already_exists_error(form.title)}, status=HTTPStatus.CONFLICT)

    author, _ = Author.objects.get_or_create(name=form.author_name, defaults={"name": form.author_name})
    work = Work(title=form.title, author=author, type=form.type)
    work.save()

    return_body = serialize_work(work.pk)

    return JsonResponse(return_body, status=HTTPStatus.ACCEPTED)


@csrf_exempt
@require_http_methods(["PATCH"])
def update_work(request, work_id):
    form = UpdateWorkForm.parse_raw(request.body)

    work = Work.objects.filter(pk=work_id).first()

    if not work:
        return_data = {"message": work_not_found_error(form.title)}
        status_code = HTTPStatus.NOT_FOUND

        return JsonResponse(return_data, status=status_code)

    if form.author_name:
        author, _ = Author.objects.get_or_create(name=form.author_name, defaults={"name": form.author_name})
        work.author = author

        if form.title and form.author_name and work_exists(form.title, form.author_name):
            return JsonResponse({"message": work_already_exists_error(form.title)}, status=HTTPStatus.CONFLICT)

    work.title = form.title if form.title else work.title
    work.type = form.type if form.type else work.type
    work.save()

    return JsonResponse(serialize_work(work.pk), status=HTTPStatus.ACCEPTED)
