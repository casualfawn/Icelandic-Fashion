from django.shortcuts import render
from item.models import Category, Item, Collections


def index(request):
    items = Item.objects.filter(is_sold=False)[0:10]
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
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()

    return render(request, 'core/Jackets.html', {
        'categories': categories,
        'items': items,
    })

def RainCoats(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()

    return render(request, 'core/RainCoats.html', {
        'categories': categories,
        'items': items,
    })

def TeesandTops(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()

    return render(request, 'core/TeesandTops.html', {
        'categories': categories,
        'items': items,
    })
def Glasses(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()

    return render(request, 'core/Glasses.html', {
        'categories': categories,
        'items': items,
    })

def Comfort(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()

    return render(request, 'core/Comfort.html', {
        'categories': categories,
        'items': items,
    })

def Sweaters(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()

    return render(request, 'core/Sweaters.html', {
        'categories': categories,
        'items': items,
    })

def HatsandScarves(request):
    items = Item.objects.filter(is_sold=False)[0:10]
    categories = Category.objects.all()

    return render(request, 'core/HatsandScarves.html', {
        'categories': categories,
        'items': items,
    })





def contact(request):
    return render(request, 'core/contact.html')

