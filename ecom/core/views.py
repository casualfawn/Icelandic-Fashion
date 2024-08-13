from django.shortcuts import render
from item.models import Category, Item, Collections
from django.db.models import Q
from django.db.models.functions import Lower


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # data = Item.objects.get(category=q)

        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) |
                                   Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            name = Category.objects.exclude(name='glasses').values_list('id', flat=True)
            return render(request, 'core/searchindex.html', {
                'data':data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })

    else:
        items = Item.objects.all()
        categories = Category.objects.all()

        return render(request, 'core/index.html', {
            'categories': categories,
            'items': items,
        })

def WestFjordsCollection(request):
    items = Item.objects.filter(collections__name='West Fjords')
    collections = Collections.objects.all()
    context = {
        'collections': collections,
        'items': items,
    }
    return render(request, 'core/WestFjordsCollection.html', context)
def EastFjordsCollection(request):
    items = Item.objects.filter(collections__name='East Fjords')
    collections = Collections.objects.all()
    context = {
        'collections':collections,
        'items':items,
    }
    return render(request, 'core/EastFjordsCollection.html', context)
def Reykjalife(request):
    items = Item.objects.filter(collections__name='Reykjalife')
    collections = Collections.objects.all()
    context = {
        'collections':collections,
        'items':items,
    }
    return render(request, 'core/Reykjalife.html', context)

def HellaMornings(request):
    items = Item.objects.filter(collections__name='Hella Mornings')
    collections = Collections.objects.all()
    context = {
        'collections':collections,
        'items':items,
    }
    return render(request, 'core/HellaMornings.html', context)


def Jackets(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # data = Item.objects.get(category=q)

        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) |  Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            return render(request, 'core/searchindex.html', {
                'data': data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })
    else:
        items = Item.objects.filter(category__name='jackets')
        categories = Category.objects.all()
        return render(request, 'core/Jackets.html', {
            'categories': categories,
            'items': items,
        })

def RainCoats(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # data = Item.objects.get(category=q)

        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) |  Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            return render(request, 'core/searchindex.html', {
                'data': data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })
    else:
        items = Item.objects.filter(category__name='rain coats')
        categories = Category.objects.all()
        return render(request, 'core/RainCoats.html', {
            'categories': categories,
            'items': items,
        })
def TeesandTops(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # data = Item.objects.get(category=q)

        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) | Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            return render(request, 'core/searchindex.html', {
                'data': data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })
    else:
        items = Item.objects.filter(category__name='shirts')
        categories = Category.objects.all()
        return render(request, 'core/TeesandTops.html', {
            'categories': categories,
            'items': items,
        })

def Glasses(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) |  Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            return render(request, 'core/searchindex.html', {
                'data': data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })
    else:
        items = Item.objects.filter(category__name='glasses')
        categories = Category.objects.all()
        return render(request, 'core/Glasses.html', {
            'categories': categories,
            'items': items,
        })
def Comfort(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # data = Item.objects.get(category=q)

        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) |  Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            return render(request, 'core/searchindex.html', {
                'data': data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })
    else:
        items = Item.objects.filter(category__name='comfort')
        categories = Category.objects.all()
        return render(request, 'core/Comfort.html', {
            'categories': categories,
            'items': items,
        })

def Sweaters(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # data = Item.objects.get(category=q)

        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) |  Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            return render(request, 'core/searchindex.html', {
                'data': data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })
    else:
        items = Item.objects.filter(category__name='sweaters')
        categories = Category.objects.all()
        return render(request, 'core/Sweaters.html', {
            'categories': categories,
            'items': items,
        })
def HatsandScarves(request):
    if 'q' in request.GET:
        q = request.GET['q']
        q = q.lower()
        # data = Item.objects.get(category=q)

        name = Lower(Category.objects.filter(name__icontains=q).values_list('id'))
        data = Item.objects.filter(Q(category__in=name) |  Q(collections__in=name))
        if len(data) == 0:
            data = Item.objects.exclude(Q(category=9))
            return render(request, 'core/searchindex.html', {
                'data': data
            })
        else:
            return render(request, 'core/searchindex.html', context={'data': data, })
    else:
        items = Item.objects.filter(category__name='hats and scarves')
        categories = Category.objects.all()
        return render(request, 'core/HatsandScarves.html', {
            'categories': categories,
            'items': items,
        })




def contact(request):
    return render(request, 'core/contact.html')

