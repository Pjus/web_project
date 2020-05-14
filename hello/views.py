from django.shortcuts import render
from django.http import HttpReaponse
# Create your views here.

def home(request):
    return HttpReaponse('Hellom Django!')

