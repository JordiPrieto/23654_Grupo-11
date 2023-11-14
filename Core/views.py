from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Core/index.html')


def productos(request):
    return render(request,'Core/productos.html')

def producto(request, productos_id):
    context = {
        'productos_id' : productos_id
        }
    return render(request, 'Core/producto.html', context)

