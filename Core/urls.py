from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .views import profile
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login', CustomLoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('register',views.register,name="register"),
    

    path('productos/',views.producto,name='productos'),
    path('contacto/',views.contacto,name='contacto')

]