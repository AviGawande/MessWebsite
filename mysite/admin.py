from django.contrib import admin
from mysite.models import Feedback
from mysite.models import Customer
from mysite.models import Menu
from mysite.models import Attendance

# Register your models here.
admin.site.register(Feedback)  

admin.site.register(Customer) 

admin.site.register(Menu)

admin.site.register(Attendance)