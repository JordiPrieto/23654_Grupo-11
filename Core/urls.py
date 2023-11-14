from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('productos/',views.productos,name='productos'),
    path('productos/producto/<producto_id>', views.producto, name='producto')
    # path('productos/<int:id>',views.productos_id,name='productos_id'),
    # path('contacto/',views.contacto,name='contacto')
]