from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    # return HttpResponse('Hello, Django!')
    name01 = request.GET['name']
    age02 = request.GET['age']
    requestDict = request.GET
    result = int(age02) + 5
    requestDict = {'result_response':result}
    return JsonResponse(requestDict)

