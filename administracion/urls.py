from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
# path('',views.index,name='index_administracion'),
path('',views.AdministracionView.as_view(), name='administracion'),
path('categoria',views.categorias_index,name='categoria'),
path('categoria_nuevo',views.CategoryCreateView.as_view(),name='categoria_nuevo'),
path('categorias/editar/<int:pk>', views.CategoriaUpdateView.as_view(), name='categorias_editar'),
path('categorias/eliminar/<int:pk>', views.CategoriaDeleteView.as_view(), name='categorias_eliminar'),
]