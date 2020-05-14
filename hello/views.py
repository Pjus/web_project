from django.shortcuts import render
from django import HttpReaponse
# Create your views here.

def home(request):
    return HttpReaponse('Hello, Django!')

