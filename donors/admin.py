from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Donor, BloodRequest

admin.site.register(Donor)
admin.site.register(BloodRequest)

