from django.contrib import admin
from .models import ServiceCategory, Service, Package, Booking
admin.site.register(ServiceCategory); admin.site.register(Service); admin.site.register(Package); admin.site.register(Booking)
