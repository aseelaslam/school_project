from django.contrib import admin

from schoolapp.models import Person, Department, Course

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Person)