from django.shortcuts import render, HttpResponse
from django import template
from django.conf import settings
# Create your views here.
import datetime

def index(request):
    return HttpResponse("<h1>يارب</h1>")

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'jobs/datetime.html', {
                                    'now': now,
                                    'template_name': 'jobs/nav.html' ,
                                    'base_dir': settings.BASE_DIR }
                                )

def profile(request, username):
    return HttpResponse("<p>Profile page of #{}</p>".format(username))


def book_category(request, category='sci-fi'):
    return HttpResponse("<p>Books in {} category</p>".format(category))


def extra_args(request, arg1, arg2):
    return HttpResponse("<p>arg1: {} <br> arg2: {} </p>".format(arg1, arg2))




def custom_response(request):
    import json
    data = {'name': 'john', 'age': 25}
    return HttpResponse(json.dumps(data), content_type='application/json')



def custom_header(request):
    res = HttpResponse('some data')
    res['content-disposition'] = 'attachment; filename=file.txt;'
    return res



def snippet_detail(request, snippet_slug):
    return HttpResponse('viewing snippet #{}'.format(snippet_slug))


def trending_snippets(request, language_slug=''):
    return HttpResponse("trending {} snippets".format(language_slug if language_slug else ""))


def tag_list(request, tag):
    return HttpResponse('viewing tag #{}'.format(tag))    
