from django.urls import path
from . import views
from django.urls import re_path as url
app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    ]