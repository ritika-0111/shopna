from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View

def index(request):
    return render(request, 'sample/index.html')




