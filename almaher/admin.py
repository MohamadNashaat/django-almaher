from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Person_Type)
admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Position)
admin.site.register(Time)
admin.site.register(Session)
admin.site.register(Session_Student)
admin.site.register(Attendance)