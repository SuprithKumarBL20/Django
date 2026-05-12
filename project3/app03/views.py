from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view3(request):
    a="<h1>this is a response from app03"
    return HttpResponse(a)

