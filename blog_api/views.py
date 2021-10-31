from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def PostList(request):
    return HttpResponse('PostList')

def PostDetail(request):
    return HttpResponse('PostDetail')
