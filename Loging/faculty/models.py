from django.db import models
from django.urls import reverse
from authorization.models import LoginFaculty

# from students.models import ThemeStudents


class FacultyUniversity(models.Model):
    NameFaculty = models.CharField(max_length=255, verbose_name='Название кафедры')
    FacultyLoginPasswords = models.ForeignKey(LoginFaculty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.NameFaculty)

    def get_absolute_url(self):
        return reverse('faculty_index', kwargs={'faculty_id': self.id})


class Specialization(models.Model):
    Name_Specialization = models.CharField(max_length=250, verbose_name='Название специальности')
    Code_Specialization = models.CharField(max_length=250, verbose_name='Код специальности')
    SpecializationFaculty = models.ForeignKey(FacultyUniversity, on_delete=models.CASCADE,
                                              verbose_name='Специализация кафедры')


# class Discip(models.Model):
#     specialization = models.ForeignKey(GroupUniversity, on_delete=models.CASCADE)
#     Code = models.CharField()
#     Name = models.CharField()
#     Times = models.DateField(blank=True, null=True, verbose_name='Дата сдача')
#     chapter = models.CharField()
#
#     def __str__(self):
#         return self.Name

# class Supervisor(models.Model):
#     First_name = models.CharField(max_length=255, verbose_name='Имя преподователя')
#     Last_name = models.CharField(max_length=255, verbose_name='Фамилия преподователя')
#     Middle_name = models.CharField(max_length=255, verbose_name='Отчество преподователя')
#     FacultyGroup = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, verbose_name='Кафедра')
#
#     def __str__(self) -> str:
#         return str(f'{self.Last_name} {self.First_name[0]} {self.Middle_name[0]}')
#
#     class Meta:
#         verbose_name = 'Преподователь'
#         verbose_name_plural = 'Преподователь'
#         db_table = 'Преподователь'
