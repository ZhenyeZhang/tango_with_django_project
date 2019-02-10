from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <vr/> <a href='/rango/about/'>About</a>")

def about(request):<a href="/rango/">Index</a>
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>View index page</a>")