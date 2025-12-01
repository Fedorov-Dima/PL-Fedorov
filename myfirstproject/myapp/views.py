from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid):
    category = request.GET.get("cat", '')
    output = "<h2>Product №{0} Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request, id, name):
    output = f"<h2>Пользователь</h2><h3>id: {id} имя: {name}</h3>"
    return HttpResponse(output)