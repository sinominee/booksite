from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart_summary.html', {"cart_products": cart_products, "quantities": quantities})


def cart_add(request):
    cart = Cart(request)
    # test the post
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup the product in DB
        product = get_object_or_404(Product, pk=product_id)

        # save to session 
        cart.add(product=product, quantity=product_qty)

        # return json response
        # response = JsonResponse({'Product Name: ': product.name})


        #get card quantity
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # GET stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete Function in Cart
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
        # return redirect('cart_summary')

