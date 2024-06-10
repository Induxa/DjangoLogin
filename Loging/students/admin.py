from django.contrib import admin
from .models import Students, Work


@admin.register(Students)
class StudentsInfo(admin.ModelAdmin):
    list_display = ['GroupStudents', 'Last_name', 'First_name', 'Middle_name']
    fields = ['GroupStudents', 'Last_name', 'First_name', 'Middle_name', 'EmailStudents', 'StudentLoginPasswords']


# @admin.register(Students)
# class StudentsInfo(admin.ModelAdmin):
#     list_display = ['GroupStudents', 'form_education', 'Status_Students', 'Last_name', 'First_name', 'Middle_name']
#     fields = ['GroupStudents', 'form_education', 'Status_Students', 'Last_name', 'First_name', 'Middle_name',
#               'EmailStudents', 'StudentLoginPasswords']


# @admin.register(ThemeStudents)
# class ThemeCourseStudents(admin.ModelAdmin):
#     list_display = ['Semester', 'Students_Themes', 'Status_themes', 'Name_themes', 'Course', 'Delivery_dates']
#     fields = ['Semester', 'Students_Themes', 'Status_themes', 'Name_themes', 'Delivery_dates', 'Course',
#               'ThemesSupervisor', 'ThemesConsultant']

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['Types_work','Name_themes', 'Course', 'Files', 'DiscipId', 'StudentId', 'statuc']
    fields = ['Types_work','Name_themes', 'Course', 'Files', 'DiscipId', 'StudentId', 'statuc']
