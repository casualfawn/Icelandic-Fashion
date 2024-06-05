from django.shortcuts import render, get_object_or_404

from .models import Item

def detail(request, pk):
    item = Item.objects.get(pk=pk)
    template = 'detail.html'
    context = {'item':item}
    related_items = Item.objects.filter(category = item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item':item,
        'related_items':related_items,

    })