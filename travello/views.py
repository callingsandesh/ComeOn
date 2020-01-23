from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'travello/about.html')

def destination(request):
    return render(request,'travello/destinations.html')

def thankyou(request):
    return render(request,'thankyou.html')
