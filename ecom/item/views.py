from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Item, Cart, CartItem
import json
import uuid
from django.views.decorators.csrf import csrf_exempt

def detail(request, pk):
    item = Item.objects.get(pk=pk)
    template = 'detail.html'
    context = {'item':item}
    related_items = Item.objects.filter(category = item.category, is_sold=False).exclude(pk=pk)[0:10]

    return render(request, 'item/detail.html', {
        'item':item,
        'related_items':related_items,

    })


def cart(request):

    return render(request, "core/cart.html")


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['id']
    product = Item.objects.get(id = product_id)
    print(product)

    try:
        cart = Cart.objects.get(session_id=request.session['nonuser'], completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        num_of_item = cart.num_of_items


    except:
        request.session['nonuser'] = str(uuid.uuid4())
        cart = Cart.objects.create(session_id=request.session['nonuser'], completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        num_of_item = cart.num_of_items

    print(cartitem)


    return JsonResponse(num_of_item, safe=False)