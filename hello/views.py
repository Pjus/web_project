from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pickle

# Create your views here.

def home(request):
    # return HttpResponse('Hello, Django!')
    x1 = request.GET['x1']
    x2 = request.GET['x2']

    emp_pkl4 = pickle.load(open('./cla.pkl', 'rb'))
    result = emp_pkl4().getPredict(int(x1), int(x2))
    requestDict = {'pre4':result}
    return JsonResponse(requestDict)

