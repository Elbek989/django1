from django.shortcuts import render

from django.http import JsonResponse
def json1(request):
    return JsonResponse({"Elbek":20})

# Create your views here.
