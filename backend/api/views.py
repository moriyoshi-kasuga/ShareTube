from django.http.response import JsonResponse


def get_hc(_):
    return JsonResponse({"status": "ok"})
