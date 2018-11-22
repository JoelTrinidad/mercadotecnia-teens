from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.urls import reverse
from .forms import billingDetailsForm

# Create your views here.
def cart(request):
    items = Item.objects.all()
    subtotal = 0.0
    if items:
        for item in items:
            subtotal+=item.total        
    total=subtotal+5
    return render(request, 'cart/cart.html', {'items':items, 'sub': subtotal, 'total': total })

def itemDelete(request, pk):
    item = get_object_or_404(Item, id=pk )
    item.delete()    
    return redirect(reverse('cart')+"?product_deleted")

def listDelete(request):
    items = Item.objects.all()
    for item in items:
        item.delete()    
    return redirect(reverse('cart')+"?list_deleted")

def checkout(request):
    # Lista de productos y total a pagar
    items = Item.objects.all()
    subtotal = 0.0
    for item in items:
        subtotal+=item.total        
    total=subtotal+5
    
    #Formulario de datos del cliente
    form = billingDetailsForm()
    context = {'items':items, 'sub': subtotal, 'total': total, 'form' : form }
    return render(request, 'cart/checkout.html', context)