from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return JsonResponse({'msg': 'This is a HomePage'})


def sex(request):
    return HttpResponse('sex')
