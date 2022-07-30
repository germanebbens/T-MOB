from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse


def get_from_cache(request, my_key):
    json_cached = cache.get(my_key)
    if json_cached:
        return JsonResponse(json_cached, safe=False)
    else:
        return HttpResponse("The '%s' key not exist or isn't active." %my_key)