from django.shortcuts import render,redirect, HttpResponseRedirect
from administracion.models import Category,Product,Tag,Employee,Client
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from .forms import CategoryForm,CategoriaForm,ProductoCreateForm,ProductoUpdateForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

class AdministracionView(PermissionRequiredMixin, TemplateView):
    template_name = 'administracion/base.html'
    permission_required = 'administracion'  # Debes definir el nombre del permiso específico

    def handle_no_permission(self):
        # Personaliza el comportamiento cuando el usuario no tiene permisos
        # En este ejemplo, redirigimos al usuario a la página de inicio
        return redirect('login')
# def index(request):
#     return render(request,'administracion/base.html')

def categorias_index(request):
    categorias = Category.objects.all()

    # if 'nombre' in request.GET:
    #     categorias = categorias.filter(nombre__contains=request.GET['nombre'])
    return render(request, 'administracion/categoria.html', {'categorias': categorias})

class CategoryCreateView(PermissionRequiredMixin,CreateView):
    model = Category
    form_class = CategoryForm  # Usa el formulario que defines en forms.py
    template_name = 'administracion/categoria_nuevo.html'
    permission_required = 'administracion'
    success_url = reverse_lazy('categoria')
    
    def handle_no_permission(self):
        return redirect('login')

class CategoriaUpdateView(UpdateView):
    model = Category
    form_class = CategoriaForm
    template_name = 'administracion/categoria_editar.html'
    success_url = reverse_lazy('categoria')

class CategoriaDeleteView(DeleteView):
    model = Category
    template_name = 'administracion/categoria_eliminar.html'
    success_url = reverse_lazy('categoria')

class ProductListView(PermissionRequiredMixin,ListView):
    model = Product
    template_name = 'administracion/producto.html'
    permission_required = 'administracion'
    context_object_name = 'products'
    
    def handle_no_permission(self):
        return redirect('login')
    
class ProductoCreateView(PermissionRequiredMixin,CreateView):
    model = Product
    template_name = 'administracion/producto_nuevo.html'
    permission_required = 'administracion'
    form_class = ProductoCreateForm
    success_url = reverse_lazy('producto')

    def handle_no_permission(self):
        return redirect('login')
    
    
class ProductUpdateView(PermissionRequiredMixin,UpdateView):
    model = Product
    template_name = 'administracion/producto_editar.html'
    permission_required = 'administracion'
    form_class = ProductoUpdateForm
    success_url = reverse_lazy('producto')

    def handle_no_permission(self):
        return redirect('login')

class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    model = Product
    template_name = 'administracion/producto_eliminar.html'
    permission_required = 'administracion'
    success_url = reverse_lazy('producto')

    def handle_no_permission(self):
        return redirect('login')