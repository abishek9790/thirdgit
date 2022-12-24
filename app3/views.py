from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function1(request):
    return HttpResponse("<h1>abishek</h1>")

def function2(request):
    return HttpResponse('hai django')
