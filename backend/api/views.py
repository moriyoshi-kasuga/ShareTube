from django.http.request import HttpRequest
from django.http.response import JsonResponse
import json

from .consts import RECIPES, TEXTURES


def get_hc(_):
    return JsonResponse({"status": "ok"})


def get_recipes(request: HttpRequest):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    value = request.GET.get("id")
    if value is None:
        return JsonResponse({"error": "Please provide recipe id"}, status=400)
    try:
        value = int(value[0])
    except ValueError:
        return JsonResponse({"error": "Invalid recipe id"}, status=400)
    value = RECIPES[value]
    if value is None:
        return JsonResponse({"error": "Recipe not found"}, status=404)
    return JsonResponse(json.dumps(value), safe=False)


def get_textures(request: HttpRequest):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)
    return JsonResponse(json.dumps(TEXTURES), safe=False)
