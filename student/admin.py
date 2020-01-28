from django.contrib import admin
from .models import *

class DetailInfoAdmin(admin.ModelAdmin):
    list_display = ('roll', 'name')


admin.site.register(StudentProfile, DetailInfoAdmin)
