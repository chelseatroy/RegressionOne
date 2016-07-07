from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def foo(request):
	return HttpResponse("Hello World!")

def bar(request):
	return HttpResponse("Bar! Baz!")
