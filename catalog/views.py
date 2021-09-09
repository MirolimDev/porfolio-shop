from django.shortcuts import render
from .models import Category, Product, Slider
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    slider = Slider.objects.all()

    last_products = []
    product_list = []

    for product in products:
        product_list.append(product)

    for i in range(1, 5):
        t = (-1)*i
        pr = product_list[t]
        last_products.append(pr)



    return render(request, 'index.html', {
        "categories": categories,
        "products": products,
        'sliders': slider,
        'last_products': last_products
    })

def product_details(request, name):
    categories = Category.objects.all()
    products = Product.objects.all()

   

    try:
        product = Product.objects.get(name=name)
         
        return render(request, 'product_detail.html', {'product': product, 'categories1': categories, 'products': products})
    except ObjectDoesNotExist:
        pass


def product_listening(request, slug):
        
    # categories = Category.objects.all()S
    
    # products1 = Product.objects.filter(slug=slug)
    
   

    try:
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(category_id=category)
        return render(request, 'product_listening.html', { 'category2': category, 'products': products})
    except ObjectDoesNotExist:
        pass