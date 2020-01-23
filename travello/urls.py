from django.urls import path
from . import views

app_name = 'travello'

urlpatterns = [
    path('',views.index,name='index'),
    path('thankyou/',views.thankyou,name='thankyou'),
    path('about/',views.about,name='about'),
    path('destination/',views.destination,name='destination'),
]
