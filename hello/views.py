from django.shortcuts import render
import django.HttpReaponse
# Create your views here.

def home(request):
    return HttpReaponse('Hello, Django!')

