from django.contrib import admin

from django.contrib import admin
from .models import Student, Course, Lecturer

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Lecturer)
