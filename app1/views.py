from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_firstapp(request):
    return HttpResponse('i am returning the string from project1 app1')

def app1_firsthtmlpage(request):
    return render(request,'muni.html')