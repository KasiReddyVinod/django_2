from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_first(resquest):
    return HttpResponse('<h1>This is app1_first source</h1')


def app1_second(resquest):
    return HttpResponse('<h2> <i> THis app1_second source</i></h2>')