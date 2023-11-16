from django.shortcuts import render
from .forms import ProductResgister

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