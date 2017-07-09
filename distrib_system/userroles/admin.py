from django.contrib import admin
from .models import Cooperator, Student, Professor, ScientificDirector, Profile

# Register your models here.
admin.site.register(Cooperator)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(ScientificDirector)
admin.site.register(Profile)