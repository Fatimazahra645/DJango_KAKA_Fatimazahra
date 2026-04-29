from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,'products/product_list.html',{'products':products})

def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'products/product_detail.html',{'product':product})

def category_list(request):
    categories = Category.objects.all()
    return render(request,'products/category_list.html',{'categories':categories})

def category_detail(request,id):
    category = get_object_or_404(Category,id=id)
    products = Product.objects.all()
    return render(request,'products/category_detail.html',{'category':category,'products':products})

@login_required
def cart(request):
    return render(request, 'products/cart.html')