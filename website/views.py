from django.shortcuts import render
from .models import Product, About
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils.translation import gettext as _


def home(request):
    obj = Product.objects.all()
    data = [
        {
            "image": img.prod_image.url
        }
        for img in obj
    ]
    json = {"response": data}
    return render(request, 'website/index.html', json)


def about(request):
    obj = About.objects.first()
    data = obj.description
    json = {"response": _(data)}
    return render(request, 'website/about.html', json)


@xframe_options_sameorigin
def contact(request):
    return render(request, 'website/contact.html')


def furniture(request):
    obj = Product.objects.filter(categories="4")
    data = [
        {
            'name': furn.prod_name,
            'description': furn.prod_description,
            'image': furn.prod_image.url
        }
        for furn in obj
    ]
    json = {"response": data}
    return render(request, 'website/furniture.html', json)


def product(request):
    obj = Product.objects.filter(categories="5")
    data = [
        {
            'name': prod.prod_name,
            'description': prod.prod_description,
            'image': prod.prod_image.url
        }
        for prod in obj
    ]
    json = {"response": data}
    return render(request, 'website/product.html', json)


def timber(request):
    obj = Product.objects.filter(categories="6")
    data = [
        {
            'name': timber.prod_name,
            'description': timber.prod_description,
            'image': timber.prod_image.url,
            'price': timber.prod_price,
            'quantity': timber.prod_quantity
        }
        for timber in obj
    ]
    json = {"response": data}
    return render(request, 'website/timber.html', json)


def application(request):
    return render(request, 'website/application.html')
