from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from Core.forms import ContactForm
from django.contrib import messages
from .models import Consulta
# from .forms import ProductResgister, RegisterCategory
# from .models import Category

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

def contacto(request):
    if request.method == 'GET':
        formulario_contacto = ContactForm()
    elif request.method == 'POST':
        formulario_contacto= ContactForm(request.POST)
        if formulario_contacto.is_valid():
            consulta = Consulta(
                nombre=formulario_contacto.cleaned_data['nombre'],
                email=formulario_contacto.cleaned_data['email'],
                asunto=formulario_contacto.cleaned_data['asunto'],
                mensaje=formulario_contacto.cleaned_data['mensaje']
            )
            consulta.save()
            messages.success(request,'Hemos recibido tu consulta')
    return render(request,'Core/contacto.html',{"contact_form":formulario_contacto})
# def register_product(request):
#     if request.method == "POST":
#         form =ProductResgister(request.POST)
#     else:
#         form =ProductResgister()
    
#     context = {
#         'register_product': form
#     }
#     return render(request, "Core/register_product.html", context)

# # class CategoryCreateView(CreateView):
# #     model = Category
# #     context_object_name = 'category_form'
# #     template_name = 'Core/category_form.html'
# #     success_url = 'category_list'
# #     form_class = RegisterCategory
# #     # fields = '__all__'


# # class CategoryListView(ListView):
# #     model = Category
# #     context_object_name = "category_list"
# #     template_name = 'Core/category_list.html'
# #     ordering = ['category_name']
# #     # systems_count = ListView.__sizeof__