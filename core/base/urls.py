from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, JsonResponse


def home(request):
    return JsonResponse({'msg': 'This is a HomePage'})


def sex(request):
    return HttpResponse('sex')


urlpatterns = [
    path('', home),
    path('sex', sex),
]
