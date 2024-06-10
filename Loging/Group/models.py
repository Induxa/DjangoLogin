from django.db import models
from faculty.models import Specialization


class GroupUniversity(models.Model):
    NameGroup = models.CharField(verbose_name='Группа')
    Year = models.CharField(verbose_name='Год')
    classification = models.CharField(verbose_name='Класификация')
    SpecializationGroup = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True,
                                            verbose_name='Cпециальность')

    def __str__(self):
        return self.NameGroup


class Discip(models.Model):
    groups = models.ForeignKey(GroupUniversity, on_delete=models.CASCADE)
    Code = models.CharField()
    Name = models.CharField()
    types_work = models.CharField(blank=True, null=True, verbose_name='Тип работы')
    Times_files = models.DateField(blank=True, null=True, verbose_name='Дата сдача работ')
    chapter = models.CharField()

    def __str__(self):
        return f"{self.Name}"
