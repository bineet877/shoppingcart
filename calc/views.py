from http.client import HTTPResponse
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html",{"name":"Bineet"})


def add(request):
    num1 = int(request.POST['val1'])
    num2 = int(request.POST['val2'])
    res = num1 + num2
    return render(request,'result.html',{'result':res})