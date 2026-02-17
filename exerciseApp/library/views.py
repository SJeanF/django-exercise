from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.

class HelloView(generic.View):
  def get(self, request, *args, **kargs):
    return HttpResponse('Hello World')