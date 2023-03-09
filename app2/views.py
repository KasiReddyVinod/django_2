from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse('<h1> <b>This is app2_first view </b></h1> ')


def app2_second(request):
    return HttpResponse('<h1> <marquee> This app2_second view </marquee></h1>')
