from django.db import models
from django.urls import reverse

from authorization.models import LoginStudents
# from datetime import datetime
from Group.models import GroupUniversity, Discip


class Students(models.Model):
    GroupStudents = models.ForeignKey(GroupUniversity, on_delete=models.SET_NULL, null=True,
                                      verbose_name='Студент группы')
    Last_name = models.CharField(max_length=255, verbose_name='Фамилия студента')
    First_name = models.CharField(max_length=255, verbose_name='Имя студента')
    Middle_name = models.CharField(max_length=255, verbose_name='Отчество студента')
    EmailStudents = models.EmailField(max_length=255, verbose_name='Почта студента', blank=True, null=True)
    StudentLoginPasswords = models.ForeignKey(LoginStudents, on_delete=models.CASCADE,
                                              verbose_name='Авторизация Студента', blank=True, null=True)

    def __str__(self) -> str:
        return str(f'{self.Last_name} {self.First_name} {self.Middle_name}')

    def get_absolute_url(self):
        return reverse('students', kwargs={'students_id': self.id})

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студентов'
        db_table = 'Студенты'


def upload_course_to(instance, filename):
    return filename


class Work(models.Model):
    Types_work = models.CharField(null=True)
    Course = models.CharField(null=True)
    Name_themes = models.CharField(null=True)
    Files = models.FileField(upload_to=upload_course_to, verbose_name='Работы', blank=True, null=True)
    statuc = models.BooleanField(default=False)
    DiscipId = models.ForeignKey(Discip, on_delete=models.CASCADE)
    StudentId = models.ForeignKey(Students, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name_themes

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        db_table = 'Темы'

