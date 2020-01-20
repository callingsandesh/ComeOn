from django.contrib import admin
from .models import Destination,TrekkingGuide,Testimonials,News,Booked

# Register your models here.
admin.site.register(Destination)


#display the list in admin panel of trekking guide
class GuideAdmin(admin.ModelAdmin):
    list_display =('name','status','email','phoneno')


admin.site.register(TrekkingGuide, GuideAdmin)


admin.site.register(Testimonials)
admin.site.register(News)
admin.site.register(Booked)