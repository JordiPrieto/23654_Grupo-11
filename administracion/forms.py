from django import forms 
from django.core.exceptions import ValidationError
from .models import Category, Employee,Product,Tag

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_tags', 'active']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_tags', 'active']

class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ProductoCreateForm, self).__init__(*args, **kwargs)
    
    widgets = {
            'description': forms.Textarea(attrs={'required': False}),  # Añade el atributo required aquí
        }

class ProductoUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
