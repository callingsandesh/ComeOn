from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('blog/',views.blog,name='blog')
]
