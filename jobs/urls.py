from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('time/',views.today_is,name='time'),
    path('user/<str:username>/',views.profile, name='profile'),
    path('books/', views.book_category, name='book_category'),
    path('books/<str:category>/',views.book_category, name='book_category'),
    path('extra/', views.extra_args, {'arg1': 1, 'arg2': (10, 20, 30)},  name='extra_args'),
]
