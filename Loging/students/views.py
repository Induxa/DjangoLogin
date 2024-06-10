import os
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from .forms import FileSaveCourse, FileSavePractice, FileSaveWCR
from .models import Students
from django.conf import settings
from django.http import HttpResponse, Http404


def student_id(request, students_id):
    from datetime import date
    studentID = get_object_or_404(Students, pk=students_id)
    students = Students.objects.filter(id=students_id)
    # course_id = ThemeStudents.objects.filter(Students_Themes=studentID).order_by('Semester', 'Status_themes')
    course = FileSaveCourse()
    practice = FileSavePractice()
    WKR = FileSaveWCR()

    if request.method == "POST":
        file_courses = FileSaveCourse(request.POST, request.FILES)
        file_practice = FileSavePractice(request.POST, request.FILES)
        file_WKR = FileSaveWCR(request.POST, request.FILES)
        date_today = date.today()
        emsil_student = request.POST.get('email_st')
        # if file_courses.is_valid():
        #     course_file = file_courses.cleaned_data['File_Course']
        #     course_semester = request.POST.get('course_sem')
        #     group_course, semester = course_semester.split('_')
        #     name_group, code_group = group_course.split('-')
        #     int_semesmter = int(semester)
        #     int_course = int(code_group[0])
        #     themes_to_update = ThemeStudents.objects.filter(
        #         Students_Themes=studentID,
        #         Semester=int_course,
        #         Status_themes=int_semesmter
        #     )
        #     if themes_to_update.exists():
        #         for themes in themes_to_update:
        #             themes.Delivery_dates = date_today
        #             themes.Course = course_file
        #             themes.save()
        #             return redirect(reverse('students:students', kwargs={'students_id': students_id}))
        #     elif not themes_to_update.exists():
        #         course_themes = ThemeStudents.objects.create(
        #             Semester=int_course,
        #             Status_themes=int_semesmter,
        #             Students_Themes=studentID,
        #             Delivery_dates=date_today,
        #             Course=course_file)
        #         course_themes.save()
        #         return redirect(reverse('students:students', kwargs={'students_id': students_id}))
        # elif file_practice.is_valid():
        #     file_practices = file_practice.cleaned_data['File_Practice']
        #     practice_semester = request.POST.get('practice_sem')
        #     group_course, semester = practice_semester.split('_')
        #     name_group, code_group = group_course.split('-')
        #     int_semesmter = int(semester)
        #     int_course = int(code_group[0])
        #     themes_to_update = ThemeStudents.objects.filter(
        #         Students_Themes=studentID,
        #         Semester=int_course,
        #         Status_themes=int_semesmter
        #     )
        #     if themes_to_update.exists():
        #         for themes in themes_to_update:
        #             themes.Delivery_dates = date_today
        #             themes.Course = file_practices
        #             themes.save()
        #     elif not themes_to_update.exists():
        #         practice_themes = ThemeStudents.objects.create(
        #             Semester=int_course,
        #             Status_themes=int_semesmter,
        #             Students_Themes=studentID,
        #             Delivery_dates=date_today,
        #             Course=file_practices)
        #         practice_themes.save()
        #         return redirect(reverse('students:students', kwargs={'students_id': students_id}))
        # elif file_WKR.is_valid():
        #     file_WKRs = file_WKR.cleaned_data['File_WKR']
        #     wkr_semester = request.POST.get('wkr_sem')
        #     group_course, semester = wkr_semester.split('_')
        #     name_group, code_group = group_course.split('-')
        #     int_semesmter = int(semester)
        #     int_course = int(code_group[0])
        #     themes_to_update = ThemeStudents.objects.filter(
        #         Students_Themes=studentID,
        #         Semester=int_course,
        #         Status_themes=int_semesmter
        #     )
        #     if themes_to_update.exists():
        #         for themes in themes_to_update:
        #             themes.Delivery_dates = date_today
        #             themes.Course = file_WKRs
        #             themes.save()
        #     elif not themes_to_update.exists():
        #         wkr_themes = ThemeStudents.objects.create(
        #             Semester=int_course,
        #             Status_themes=int_semesmter,
        #             Students_Themes=studentID,
        #             Delivery_dates=date_today,
        #             Course=file_WKRs)
        #         wkr_themes.save()
        #         return redirect(reverse('students:students', kwargs={'students_id': students_id}))
        # elif emsil_student:
        #     email_update = Students.objects.get(pk=students_id)
        #     email_update.EmailStudents = emsil_student
        #     email_update.save()
        #     return redirect(reverse('students:students', kwargs={'students_id': students_id}))
    date = {
        'id': students_id,
        'student': studentID,
        'students': students,
        # 'themes': course_id,
        'Course': course,
        'Practice': practice,
        'WKR': WKR
    }
    return render(request, 'students/indexStudent.html', context=date)


def download(request, students_id):
    # Починить скачивание архива rar
    if request.method == 'POST':
        cr = request.POST.get('course')
        file_extension = os.path.splitext(cr)[1].lower()
        if file_extension == '.zip':
            content_type = 'application/zip'
        elif file_extension == '.rar':
            content_type = 'application/x-rar-compressed'
        else:
            content_type = 'application/octet-stream'

        file_path = os.path.join(settings.MEDIA_ROOT, cr)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=content_type)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404
