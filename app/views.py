from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def srujana(request):
    return HttpResponse('<h1><marquee>Tinnava raaa....</marquee></h1>')
def divya(request):
    return HttpResponse('<h1><marquee>divya waste fellow tinnava raaa....</marquee></h1>')
