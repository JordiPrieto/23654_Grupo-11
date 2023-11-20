from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    

    path('productos/',views.productos,name='productos'),
    path('productos/producto/<producto_id>', views.producto, name='producto'),
    path('contacto/',views.contacto,name='contacto')
    # path('productos/registrar_producto', views.register_product, name='register_product_form'),

    # path('category_form', views.CategoryCreateView.as_view(), name="category_form"),
    # path('category_list', views.CategoryListView.as_view(), name='category_list')

    # path('productos/<int:id>',views.productos_id,name='productos_id'),
    # path('contacto/',views.contacto,name='contacto')
]