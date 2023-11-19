from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Employee


class ProductResgister(forms.Form):
    prod_name = forms.CharField(max_length=45, label="Nombre del producto: ", widget=forms.TextInput(attrs={'class':'red_background'}), required=True)
    
    category = forms.CharField(max_length=30, label="Categoría: ")

    stock = forms.IntegerField(label="Stock inicial: ", required=False)
    
    price = forms.FloatField(label="Precio por unidad: ", required=False)

    visible = forms.BooleanField(label="Hacer visible a clientes? ", required=False)

    active = forms.BooleanField(label="Activo?", required=False)

    description = forms.CharField(widget=forms.Textarea, label="Descripción: ", required=False)

    image = forms.URLField(label = "URL de la imagen: ", required=False)

    def clean_age(self):
        if self.cleaned_data["price"] < 0:
            raise ValidationError("Un producto no puede tener un precio negativo")
        return self.cleaned_data["price"]

    def clean(self):
        if self.cleaned_data['stock'] < 0:
            raise ValidationError("No se puede tener un stock inicial negativo")
        return self.cleaned_data


class RegisterCategory(forms.ModelForm):    

    class Meta:
        model = Category
        fields = '__all__'

    def clean_category_name(self):
        if len(self.cleaned_data['category_name']) < 1:
            raise ValidationError('Category name cannot be empty')

        return self.cleaned_data['category_name']
    
    
class RegisterEmployee(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

    def clean_employee_number(self):
        if len(self.cleaned_data['employee_number']) < 1:
            raise ValidationError('Employee number must be a unique positive number')
        
        return self.cleaned_data['employee_number']
