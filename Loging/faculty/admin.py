from django.contrib import admin
from .models import FacultyUniversity, Specialization


@admin.register(FacultyUniversity)
class Faculty(admin.ModelAdmin):
    list_display = ['NameFaculty']
    fields = ['NameFaculty', 'FacultyLoginPasswords']


@admin.register(Specialization)
class Specializations(admin.ModelAdmin):
    list_display = ['Name_Specialization', 'Code_Specialization']
    fields = ['Name_Specialization', 'Code_Specialization', 'SpecializationFaculty']


# @admin.register(Supervisor)
# class Supervisors(admin.ModelAdmin):
#     list_display = ['FacultyGroup', 'Last_name', 'First_name', 'Middle_name']
#     fields = ['FacultyGroup', 'Last_name', 'First_name', 'Middle_name']
