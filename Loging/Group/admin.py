from django.contrib import admin
from .models import GroupUniversity, Discip


@admin.register(GroupUniversity)
class Group(admin.ModelAdmin):
    list_display = ['NameGroup', 'SpecializationGroup', 'classification', 'Year']
    fields = ['NameGroup', 'SpecializationGroup', 'classification', 'Year']


@admin.register(Discip)
class Discip(admin.ModelAdmin):
    list_display = ['groups', 'Code', 'Name', 'types_work', 'chapter', 'Times_files']
    fields = ['groups', 'Code', 'Name', 'types_work', 'chapter', 'Times_files']
