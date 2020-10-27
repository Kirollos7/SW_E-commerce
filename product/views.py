from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request, 'product/product.html',{})

def product_detail(request):
    
    return render(request, 'product/product_detail.html',{})