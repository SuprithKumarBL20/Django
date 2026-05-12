from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    a="this is a response from app01"
    return HttpResponse(a)