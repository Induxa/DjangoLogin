from django.db import models


class LoginFaculty(models.Model):
    Login_faculty = models.CharField(max_length=250)
    Password_faculty = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Авторизация кафедры'
        verbose_name_plural = 'Авторизация кафедры'
        db_table = 'Авторизация кафедры'


class LoginStudents(models.Model):
    Login_Student = models.CharField(max_length=250)
    Password_Student = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Авторизация студента'
        verbose_name_plural = 'Авторизация студента'
        db_table = 'Авторизация студента'

# class Deportament(models.Model):
#     Name_Deportament = models.CharField(max_length=250, verbose_name='Название кафедры')
#     Code_Deportament = models.CharField(max_length=250, verbose_name='Код кафедры')
#     Login_Deportament = models.CharField(max_length=250)
#     Password_Deportament = models.CharField(max_length=250)
#
#     def __str__(self) -> str:
#         return str(self.Name_Deportament)
#
#     class Meta:
#         verbose_name = 'Кафедра'
#         verbose_name_plural = 'Кафедры'
#         db_table = 'Кафедры'


# class Specialization(models.Model):
#     Name_Specialization = models.CharField(max_length=250, verbose_name='Название специальности')
#     Code_Specialization = models.CharField(max_length=250, verbose_name='Код специальности')
#     Specialization_Deportament = models.ForeignKey(Deportament, on_delete=models.CASCADE,
#                                                    verbose_name='Специализация кафедры')
#
#     def __str__(self) -> str:
#         return self.Name_Specialization
#
#     class Meta:
#         verbose_name = 'Специальность'
#         verbose_name_plural = 'Специальности'
#         db_table = 'Специальности'
#
#
# class Group(models.Model):
#     Name_Group = models.CharField(max_length=100, verbose_name='Название группы')
#     Group_Specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,
#                                              verbose_name='Группа специальности')
#
#     def __str__(self) -> str:
#         return self.Name_Group
#
#     class Meta:
#         verbose_name = 'Группа'
#         verbose_name_plural = 'Группы'
#         db_table = 'Группы'
#
#
# class Student(models.Model):
#     First_Name = models.CharField(max_length=100, verbose_name='Имя студента')
#     Last_Name = models.CharField(max_length=100, verbose_name='Фамилия студента')
#     Patronymic = models.CharField(max_length=100, verbose_name='Отчество студента')
#     Login_Student = models.CharField(max_length=250)
#     Password_Student = models.CharField(max_length=250)
#     Groups = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
#
#     def __str__(self) -> str:
#         return f"{self.First_Name} {self.Last_Name} {self.Patronymic}"
#
#     class Meta:
#         verbose_name = 'Студент'
#         verbose_name_plural = 'Студенты'
#         db_table = 'Студенты'
#
#
# class Thema(models.Model):
#     Name_Theme = models.CharField(max_length=250, verbose_name='Название темы')
#     Theme_Student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
#
#     def __str__(self) -> str:
#         return self.Name_Theme
#
#     class Meta:
#         verbose_name = 'Тема'
#         verbose_name_plural = 'Темы'
#         db_table = 'Темы'
#
#
# class Teacher(models.Model):
#     First_Name = models.CharField(max_length=100, verbose_name='Имя преподователя')
#     Last_Name = models.CharField(max_length=100, verbose_name='Фамилия преподователя')
#     Patronymic = models.CharField(max_length=100, verbose_name='Отчество преподователя')
#     Theme_Teacher = models.ForeignKey(Thema, on_delete=models.CASCADE, verbose_name='Руководитель темы')
#     Teacher_Departament = models.ForeignKey(Deportament, on_delete=models.CASCADE, verbose_name='Сотрудник кафедры')
#
#     def __str__(self) -> str:
#         return f"{self.First_Name} {self.Last_Name} {self.Patronymic}"
#
#     class Meta:
#         verbose_name = 'Преподователь'
#         verbose_name_plural = 'Преподователи'
#         db_table = 'Преподователи'
#
#
# class Consultant(models.Model):
#     First_Name = models.CharField(max_length=100, verbose_name='Имя консультанта')
#     Last_Name = models.CharField(max_length=100, verbose_name='Фамилия консультанта')
#     Patronymic = models.CharField(max_length=100, verbose_name='Отчество консультанта')
#     Theme_Consultant = models.ForeignKey(Thema, on_delete=models.CASCADE, verbose_name='Консультант темы')
#     Consultant_Deportament = models.ForeignKey(Deportament, on_delete=models.CASCADE,
#     verbose_name='Сотрудник кафедры')
#
#     def __str__(self) -> str:
#         return f"{self.First_Name} {self.Last_Name} {self.Patronymic}"
#
#     class Meta:
#         verbose_name = 'Консультант'
#         verbose_name_plural = 'Консультанты'
#         db_table = 'Консультанты'
