from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says HEELLOO!!! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says this is the about page. <a href='/rango/'>Index</a>")
