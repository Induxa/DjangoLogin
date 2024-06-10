# from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import Login
from .models import LoginFaculty, LoginStudents


def index(request):
    user = Login(request.POST)
    if request.method == "POST":
        if user.is_valid():
            logins = user.cleaned_data['login']
            password = user.cleaned_data['password']
            try:
                student = LoginStudents.objects.get(Login_Student=logins)
                return HttpResponseRedirect(reverse('students:students', args=[student.id]))
            except LoginStudents.DoesNotExist:
                pass
            try:
                facultys = LoginFaculty.objects.get(Login_faculty=logins)
                return HttpResponseRedirect(reverse('faculty:faculty_index', args=[facultys.id]))
            except LoginFaculty.DoesNotExist:
                pass
    return render(request, 'autoriz/index.html', {'User': Login})
