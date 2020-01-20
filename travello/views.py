from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination,TrekkingGuide,Testimonials,News,Booked
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    dests=Destination.objects.all()
    testimonials=Testimonials.objects.all()
    news=News.objects.all()
    return render(request,'index.html',{'dests':dests,'testimonials':testimonials,'news':news})

def guides(request):
    trek_guide=TrekkingGuide.objects.all()
    return render(request,'guides.html',{'guides':trek_guide})

def destinations(request):
    
    
    dest_id=request.POST['dest_id']
    
    dests=Destination.objects.get(pk=dest_id)




    return render(request,'destinations.html',{'dest':dests})

def booking(request):
    dest_id=request.POST['dest_id']
    return render(request,'booking.html',{'dest_id':dest_id})


def booked(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone_no=request.POST['phone_no']
        dest_id=request.POST['dest_id']
        
        
        guide=TrekkingGuide.objects.get(pk=4)
        
        if Booked.objects.filter(phone_no=phone_no).exists():
                messages.info(request,'you have already booked from this phone-number')
                return render(request,'booking.html')
            
        else:
                #confirmation email sending to user
            subject = "Thank you for Booking from our site"
            message =  "Congratulation "+ first_name + ". Your trekking has been sucessyfully booked and the trekking guide "+ guide.name +" has been appointed to you"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
           
            #confirmation email sending to trekking guide
            guide_email=guide.email
            subject = "You have been appointed a guest for trekking"
            message =  "The person named  "+ first_name + "   has been apponted to you for guiding"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [guide_email]
            send_mail( subject, message, email_from, recipient_list )



           
            
            user=Booked(first_name=first_name,last_name=last_name,email=email,phone_no=phone_no)
            user.save()
            dest=Destination.objects.get(pk=dest_id)
            return render(request,'conformation.html',{'dest':dest,'guide':guide})

                
    
        
        
        



      

        
    
    

