from django.forms import forms


class FileSaveCourse(forms.Form):
    File_Course = forms.FileField()


class FileSavePractice(forms.Form):
    File_Practice = forms.FileField()


class FileSaveWCR(forms.Form):
    File_WKR = forms.FileField()
