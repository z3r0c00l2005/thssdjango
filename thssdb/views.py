from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def home(request):
    return render(request, 'home.html')
