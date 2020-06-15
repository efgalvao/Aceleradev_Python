from django.urls import path

from . import views

urlpatterns = [
    path('solfi/', views.solfi, name='solfi'),
    path('', views.solfi, name='index'),
    #path('catalogs/', views.solfi, name='solfi'),
    

]
