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

path('producto',views.ProductListView.as_view(),name='producto'),
path('producto/nuevo',views.ProductoCreateView.as_view(),name='producto_nuevo'),
path('producto/editar/<int:pk>',views.ProductUpdateView.as_view(),name='producto_editar'),
path('producto/eliminar/<int:pk>',views.ProductDeleteView.as_view(),name='producto_eliminar'),

path('etiqueta',views.TagListView.as_view(),name='tag'),
path('etiqueta/nuevo',views.TagCreateView.as_view(),name='tag_nuevo'),
path('etiqueta/editar/<int:pk>',views.TagUpdateView.as_view(),name='tag_editar'),
path('etiqueta/eliminar/<int:pk>',views.TagDeleteView.as_view(),name='tag_eliminar'),
]