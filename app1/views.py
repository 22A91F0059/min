from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def project(request):
    return HttpResponse('started project')
def sateesh(request):
    return HttpResponse('sateesh chandra')