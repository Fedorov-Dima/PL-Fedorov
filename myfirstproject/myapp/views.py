from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    data = {"message": "Пример простых данных"}
    return render(request, "index.html", context=data)

def about(request):
    return render(request, "about.html")

def contact(request):
    langs = ["Python", "Java", "1С"]
    user = {"name": "Tom", "age": 23}
    adress = ("Абрикосовая", 23, 45)
    data = {"langs": langs, "user": user, "adress": adress}
    return render(request, "contact.html", context=data)

def statfiles(request):
    return render(request, "statfiles.html")

def formhtml(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname", "Undefined")
        lastname = request.POST.get("lastname", "Undefined")
        patronymic = request.POST.get("patronymic", "Undefined")
        age = request.POST.get("age", 1)
        adress = request.POST.get("adress", "Undefined")
        group = request.POST.get("group", "У-242")
        exams = request.POST.getlist("exams", ['Технологии программирования'])
        data = {"firstname": firstname, "lastname": lastname, "patronymic": patronymic, "age": age, "adress": adress,
                "group": group, "exams": exams}
        return render(request, "form_html_view.html", context=data)
    else:
        return render(request, "form_html.html")

def fields(request):
    userformfields = UserFormFields()
    return render(request, "fields.html", {"formfields": userformfields})

def userdata(request):
    userformdata = UserFormData()
    return render(request, "fields.html", {"formfields": userformdata})