from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "Simple/index.html",
        {
            'title':"Hello Django",
            'message':"Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y %X")
        }
        )

def about(request):
    return render(
        request,
        "Simple/about.html",
        {
            'title': "About Simple",
            'content': "Example app page for Django."
            }
        )

# Create your views here.
