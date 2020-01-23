from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request,'blogs/blogs.html')
