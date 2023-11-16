from django import forms
from django.core.exceptions import ValidationError


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
        if self.cleaned_data["pricce"] < 0:
            raise ValidationError("Un producto no puede tener un precio negativo")
        return self.cleaned_data["price"]

    def clean(self):
        if self.cleaned_data['stock'] < 0:
            raise ValidationError("No se puede tener un stock inicial negativo")
        return self.cleaned_data


