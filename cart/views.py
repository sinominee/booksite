from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    return render(request, 'cart_summary.html', {})


def cart_add(request):
    cart = Cart(request)
    # test the post
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))

        # lookup the product in DB
        product = get_object_or_404(Product, pk=product_id)

        # save to session 
        cart.add(product=product)

        # return json response
        response = JsonResponse({'Product Name: ': product.name})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
