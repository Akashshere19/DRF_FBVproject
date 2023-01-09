from django.contrib import admin
from .models import Course
# Register your models here.
class AdminCourse(admin.ModelAdmin):
    list_display = ['name','author','price','discount','duration']

admin.site.register(Course,AdminCourse)    