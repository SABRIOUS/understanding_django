from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('',views.index,name='index'),
    path('time/',views.today_is,name='time'),
    #dynamic Url write whatever you want to pass user/ahmed for example
    path('user/<str:username>/',views.profile, name='profile'),
    path('books/', views.book_category, name='book_category'),
    path('books/<str:category>/',views.book_category, name='book_category'),
    path('extra/', views.extra_args, {'arg1': 1, 'arg2': (10, 20, 30)},  name='extra_args'),
    path('trending/', views.trending_snippets, name='trending_snippets'),
    path('trending/<str:language_slug>/', views.trending_snippets, name='trending_snippets'),
    path('<slug:snippet_slug>', views.snippet_detail, name='snippet_detail'),
    path('tag/<str:tag>/', views.tag_list, name='tag_list'),

]
