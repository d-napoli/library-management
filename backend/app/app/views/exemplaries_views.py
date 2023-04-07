import json
from http import HTTPStatus

from app.constants.exemplaries_constants import exemplary_already_active_error, exemplary_not_found
from app.constants.work_constants import work_not_found_by_id_error
from app.forms.exemplaries_forms import AddExemplaryForm
from app.models import Exemplary, Work
from app.services.exemplaries_svc import serialize_exemplary
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@csrf_exempt
@require_GET
def list_all_exemplaries(request):
    all_exemplaries = Exemplary.objects.filter(is_active=True).order_by("pk")
    data = json.dumps([serialize_exemplary(e) for e in all_exemplaries])
    return JsonResponse({"exemplaries": json.loads(data)})


@csrf_exempt
@require_http_methods(["DELETE"])
def remove_exemplary(request, exemplary_id):
    exemplary = Exemplary.objects.filter(pk=exemplary_id, is_active=True).first()

    if exemplary:
        exemplary.is_active = False
        exemplary.save()

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)
    else:
        return JsonResponse({"message": exemplary_not_found()}, status=HTTPStatus.NOT_FOUND)


@csrf_exempt
@require_http_methods(["PATCH"])
def reactivate_exemplary(request, exemplary_id):
    try:
        exemplary = Exemplary.objects.get(pk=exemplary_id)

        if exemplary.is_active:
            return JsonResponse({"message": exemplary_already_active_error()}, status=HTTPStatus.CONFLICT)

        exemplary.is_active = True
        exemplary.save()

        return JsonResponse({}, status=HTTPStatus.ACCEPTED)

    except Exemplary.DoesNotExist:
        return JsonResponse({"message": exemplary_not_found()}, status=HTTPStatus.NOT_FOUND)


@csrf_exempt
@require_POST
def add_exemplary(request):
    form = AddExemplaryForm.parse_raw(request.body)

    try:
        work = Work.objects.get(pk=form.work_id)
        exemplary = Exemplary(work=work)
        exemplary.save()

        return JsonResponse(serialize_exemplary(exemplary), status=HTTPStatus.CREATED)
    except Work.DoesNotExist:
        return JsonResponse({"message": work_not_found_by_id_error(form.work_id)}, status=HTTPStatus.NOT_FOUND)
