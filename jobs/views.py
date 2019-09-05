from django.shortcuts import render, HttpResponse

# Create your views here.
import datetime

def index(request):
    return HttpResponse("<h1>يارب</h1>")

def today_is(request):
        now = datetime.datetime.now()
        html = "Current date {0}".format(now)
        return HttpResponse(html)

def profile(request, username):
    return HttpResponse("<p>Profile page of #{}</p>".format(username))


def book_category(request, category='sci-fi'):
    return HttpResponse("<p>Books in {} category</p>".format(category))


def extra_args(request, arg1, arg2):
    return HttpResponse("<p>arg1: {} <br> arg2: {} </p>".format(arg1, arg2))    
