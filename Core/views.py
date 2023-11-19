from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import ProductResgister, RegisterCategory
from .models import Category

# Create your views here.

def index(request):
    return render(request,'Core/index.html')


def productos(request):
    return render(request,'Core/productos.html')

def producto(request, producto_id):
    context = {
        'producto_id' : producto_id
        }
    return render(request, 'Core/producto.html', context)

def register_product(request):
    if request.method == "POST":
        form =ProductResgister(request.POST)
    else:
        form =ProductResgister()
    
    context = {
        'register_product': form
    }
    return render(request, "Core/register_product.html", context)

class CategoryCreateView(CreateView):
    model = Category
    context_object_name = 'category_form'
    template_name = 'Core/category_form.html'
    success_url = 'category_list'
    form_class = RegisterCategory
    # fields = '__all__'


class CategoryListView(ListView):
    model = Category
    context_object_name = "category_list"
    template_name = 'Core/category_list.html'
    ordering = ['category_name']
    # systems_count = ListView.__sizeof__