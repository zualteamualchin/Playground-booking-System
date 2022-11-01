from django.contrib import admin
from .models import Customer, Location,Scheduler,Booked,Manager
# Register your models here.

admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Scheduler)
admin.site.register(Booked)
admin.site.register(Manager)
