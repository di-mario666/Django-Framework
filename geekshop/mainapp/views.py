from django.shortcuts import render
from django.conf import settings
import os
from mainapp.models import Product

def main(request):
    title = 'Главная'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    title = 'продукты'
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
    content = {'title': title, 'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)

def contact(request):
    content = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contact.html', content)

def products_all(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
    content = {
        'title': 'Продукт',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)

def products_home(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
    content = {
        'title': 'Продукт',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)

def products_modern(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
    content = {
        'title': 'Продукт',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)

def products_office(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
    content = {
        'title': 'Продукт',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)

def products_classic(request):
    links_menu = [
        {'href': 'products_all', 'name': 'Все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_classic', 'name': 'классик'},
    ]
    content = {
        'title': 'Продукт',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', content)