
from django.contrib import admin
from django.urls import path, include
from core.views import (index, contact,
    WestFjordsCollection, EastFjordsCollection,
    Reykjalife, HellaMornings, Jackets, RainCoats,
    TeesandTops, Glasses, Comfort, Sweaters,
                        HatsandScarves)
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path as url

urlpatterns = [
    path('', index, name='index'),
    path('items/', include('item.urls')),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
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
