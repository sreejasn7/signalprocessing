from django.contrib import admin

# Register your models here.
from .models import Detail_measurements , Measurements

admin.site.register(Detail_measurements)
admin.site.register(Measurements)

