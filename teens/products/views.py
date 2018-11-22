from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from cart.models import Item
from .forms import QuantityForm
from django.urls import reverse_lazy, reverse
from cart.models import Item

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {'product_list' : products})

def product(request, pk, slug):
    quantity_form = QuantityForm()
    product = get_object_or_404(Product, id = pk)
    if request.method == "POST":
        quantity_form = QuantityForm(data=request.POST)
        if quantity_form.is_valid():
            quantity = int(request.POST.get('quantity', ''))
            items = Item.objects.all()
            for item in items:
                if product.name == item.product.name:
                    item.quantity += quantity
                    item.total = product.price*item.quantity
                    item.save()
                    return redirect(reverse('cart')+"?quantity")
            item = Item(product=product, quantity=quantity, total=product.price*quantity )
            try:
                item.save()
                return redirect(reverse_lazy('cart'))
            except:
                return redirect(reverse('products:products')+"?fail")
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'form':quantity_form,})
    