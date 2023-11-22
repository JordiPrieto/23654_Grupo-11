from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from Core.forms import ContactForm
from django.contrib import messages
from .models import Consulta
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from administracion.models import Product
# from .forms import ProductResgister, RegisterCategory
# from .models import Category

# Create your views here.

def index(request):
    productos_destacados = Product.objects.filter(product_tags__tag_name='destacado')
    # Pasa los productos destacados al contexto
    context = {
        'productos_destacados': productos_destacados
    }

    return render(request, 'Core/index.html', context)

def profile(request):
    return render(request, 'Core/profile.html')


def producto(request):
    tag_filtro = request.GET.get('tag', None)

    # Filtra los productos según el tag (si hay un tag)
    if tag_filtro:
        productos_filtrados = Product.objects.filter(product_tags__tag_name=tag_filtro)
    else:
        # Si no hay tag seleccionado, muestra todos los productos
        productos_filtrados = Product.objects.all()

    context = {
        'productos_filtrados': productos_filtrados,
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



class CustomLoginView(LoginView):
    template_name = 'core/login.html' 

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request,"Core/register.html",{"form":form})


