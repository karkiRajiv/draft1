from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm
# Create your views here.
from django.urls import reverse
#
# def myview(request):
#     return HttpResponseRedirect(reverse('arch-summary', args=[1945]))
#
#


def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category =  category )
    return render(request, 'shop.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request ,id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available= True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def show_shops(request):
    return render(request,'shop.html')
