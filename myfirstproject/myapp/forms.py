from django import forms
from django.forms import CheckboxSelectMultiple


class UserFormFields(forms.Form):
    BooleanField = forms.BooleanField()
    NullBooleanField = forms.NullBooleanField()
    CharField = forms.CharField(min_length=2, max_length=20)
    IntegerField = forms.IntegerField(min_value=1, max_value=100)
    DecimalField = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    FloatField = forms.FloatField()
    EmailField = forms.EmailField()
    GenericIPAddressField = forms.GenericIPAddressField()
    URLField = forms.URLField()
    FileField = forms.FileField()
    ImageField = forms.ImageField()
    DateField = forms.DateField()
    TimeField = forms.TimeField()
    DateTimeField = forms.DateTimeField()
    DurationField = forms.DurationField()
    ChoiceField = forms.ChoiceField(choices=((1, "Python"), (2, "C++"), (3, "C#")))
    MultipleChoiceField = forms.MultipleChoiceField(choices=((1, "Python"), (2, "C++"), (3, "C#")))


BIRT_YEAR_CHOICES = ['2001', '2002', '2003', '2004', '2005', '2006']
class UserFormData(forms.Form):
    name = forms.CharField(label='Имя', help_text='Введите свое ФИО:', min_length=2)
    age = forms.IntegerField(min_value=1, max_value=100, label='Возраст', initial=1, help_text='Введите свой возраст:')
    group = forms.CharField(label='Группа', help_text='Введите номер группы:')
    birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRT_YEAR_CHOICES),
                            label='Дата рождения', help_text='Введите дату рождения:')
    languages = forms.ChoiceField(choices=((1, "Python"), (2, "C++"), (3, "C#")))
    email = forms.EmailField()

