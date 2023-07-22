from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>Ragnor lathbrok king of kattegat 1</h1>')
def second(request):
    return HttpResponse('<h1>lagertha shield maiden 1</h1>')
