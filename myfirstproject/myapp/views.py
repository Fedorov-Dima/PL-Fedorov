from django.shortcuts import render
from django.http import HttpResponse

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

def products(request, productid):
    category = request.GET.get("cat", '')
    output = "<h2>Product №{0} Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request, id, name):
    output = f"<h2>Пользователь</h2><h3>id: {id} имя: {name}</h3>"
    return HttpResponse(output)