
from django.contrib import admin
from django.urls import path, include
from core.views import (index, contact, NewItems,
    WestFjordsCollection, EastFjordsCollection,
    Reykjalife, HellaMornings, Jackets, RainCoats,
    TeesandTops, Glasses, Comfort, Sweaters,
                        HatsandScarves)

from item.views import cart, add_to_cart
from search.views import SearchView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path as url
from django.urls import path
from search import views
urlpatterns = [


              #  path('cart', cart, name = 'cart'),

                #  path("add_to_cart", add_to_cart, name="add"),
#
                  #  path('search/', SearchView, name='search'),
                  path('', index, name='index'),
                  path('items/', include('item.urls')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),

    path('NewItems/', NewItems, name = 'NewItems'),
    path('WestFjordsCollection/', WestFjordsCollection, name='WestFjordsCollection'),
    path('EastFjordsCollection/', EastFjordsCollection, name='EastFjordsCollection'),
    path('Reykjalife/', Reykjalife, name='Reykjalife'),
    path('HellaMornings/', HellaMornings, name='HellaMornings'),

    path('Jackets/', Jackets, name='Jackets'),
                  path('RainCoats/', RainCoats, name='RainCoats'),
                  path('Sweaters/', Sweaters, name='Sweaters'),
                  path('TeesandTops/', TeesandTops, name='TeesandTops'),
                  path('Glasses/', Glasses, name='Glasses'),
                  path('Comfort/', Comfort, name='Comfort'),
                  path('HatsandScarves/', HatsandScarves, name='HatsandScarves'),

              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
