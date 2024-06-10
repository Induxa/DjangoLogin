from django.contrib import admin
from .models import LoginFaculty, LoginStudents
# from django.contrib.auth.hashers import make_password

admin.site.register(LoginFaculty)
admin.site.register(LoginStudents)

# class SpecializationAdmin(admin.ModelAdmin):
#     list_display = ('Name_Specialization', 'Code_Specialization')
#     fields = ('Name_Specialization', 'Code_Specialization', 'Specialization_Deportament')
#
# admin.site.register(Specialization, SpecializationAdmin)
#
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('Name_Group')
#     fields = ('Name_Group', 'Group_Specialization')
#
# admin.site.register(Group, GroupAdmin)
#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('First_Name', 'Last_Name', 'Patronymic')
#     fields = ('First_Name', 'Last_Name', 'Patronymic', 'Groups', 'Login_Student', 'Password_Student')
#
#     def save_model(self, request, obj, form, change):
#         obj.Password_Student = make_password(obj.Password_Student)
#         super().save_model(request, obj, form, change)
#
# admin.site.register(Student, StudentAdmin)
#
# class ThemaAdmin(admin.ModelAdmin):
#     list_display = ('Name_Theme',)
#     fields = ('Name_Theme', 'Theme_Student')
#
# admin.site.register(Thema, ThemaAdmin)
#
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('First_Name', 'Last_Name', 'Patronymic')
#     fields = ('First_Name', 'Last_Name', 'Patronymic', 'Theme_Teacher', 'Teacher_Departament')
#
# admin.site.register(Teacher, TeacherAdmin)
#
# class ConsultantAdmin(admin.ModelAdmin):
#     list_display = ('First_Name', 'Last_Name', 'Patronymic')
#     fields = ('First_Name', 'Last_Name', 'Patronymic', 'Theme_Consultant', 'Consultant_Deportament')
#
# admin.site.register(Consultant, ConsultantAdmin)
