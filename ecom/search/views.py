from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from item.models import Item, Category
from django.db.models import Q
from django.views.generic.list import ListView
# Create your views here.
from requests import request


def SearchView(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
       # data = Item.objects.get(category=q)

        name = Category.objects.filter(name__icontains=q).values_list('id', flat=True)
        name = name.lower()
        data = Item.objects.filter(Q(category__icontains=name) |
                                            Q(collections__icontains=name))


        # multiple_q = Q(Q(category__icontains=q) | Q(collections__icontains=q))
       # data = Item.objects.filter(multiple_q)
    else:
        data = Item.objects.all()
    context = {
        'data': data
    }
    return render(request, 'core/searchindex.html', context)
    #return redirect(f'/search_results/?query')