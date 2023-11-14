from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Core/index.html')


def productos(request):
    return render(request,'Core/productos.html')

def producto(request, item):
    context = {
        'item' : item
        }
    return render(request, 'Core/producto.html', context)