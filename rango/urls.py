from django.conf.urls import url
from django.urls.conf import path
from rango import views
urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about')
]