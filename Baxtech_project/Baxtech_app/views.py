from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Baxtech_app\\index.html')

def products(request, inicio):
    return render(request, 'Baxtech_app\\products.html')

def cart(request):
    return HttpResponse("Carrito")

def about_us(request):
    return render(request, 'Baxtech_app\\about_us.html')