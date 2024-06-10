from django import forms
# from .models import Specialization


class AllDateStudent(forms.Form):
    OPTION_CHOICES = [
        ('AllDateStudent', 'Все данные'),
    ]
    allDateRadio = forms.ChoiceField(label='Вывод данных', choices=OPTION_CHOICES, widget=forms.RadioSelect(attrs={'name': 'AllDate'}))


class GroupDateStudent(forms.Form):
    OPTION_CHOICES = [
        ('GroupDateStudent', 'Данные по группе'),
    ]
    groupDateRadio = forms.ChoiceField(choices=OPTION_CHOICES, widget=forms.RadioSelect(attrs={'name': 'group'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groupDateRadio'].widget.attrs.update({
            'class': 'group_find',
        })

class DateStudent(forms.Form):
    OPTION_CHOICES = [
        ('StudentDate', 'Данные по студенту'),
    ]
    studetnDateRadio = forms.ChoiceField(choices=OPTION_CHOICES, widget=forms.RadioSelect)


class AddFile(forms.Form):
    Files = forms.FileField(widget=forms.FileInput(attrs={'accept': '.xlsx, .docx'}))
