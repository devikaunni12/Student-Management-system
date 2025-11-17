from django.contrib import admin
from .models import Department, Student, Profile, Course

# Register your models here.
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Course)
