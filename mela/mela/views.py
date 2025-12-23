from django.shortcuts import render
from main.models import Product
def index(request):

    s_products = Product.objects.all()

    return render(request,'index.html', {
        "s_products": s_products
    })
