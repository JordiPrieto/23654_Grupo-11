from django import forms
from django.core.exceptions import ValidationError


class ProductResgister(forms.Form):
    prod_name = forms.CharField(max_length=45, label="Product name: ", widget=forms.TextInput(attrs={'class':'red_background'}), required=True)
    
    category = forms.CharField(max_length=30, label="Category: ")

    stock = forms.IntegerField(label="Initial stock: ", required=False)
    
    price = forms.FloatField(label="Price per unit: ", required=False)

    visible = forms.BooleanField(label="Make visible to customers? ", required=False)

    active = forms.BooleanField(label="Active?", required=False)

    description = forms.CharField(widget=forms.Textarea, label="Description: ", required=False)

    image = forms.URLField(label = "Image's URL: ", required=False)

    def clean_age(self):
        if self.cleaned_data["pricce"] < 0:
            raise ValidationError("Character can't have a negative price")
        return self.cleaned_data["age"]

    def clean(self):
        if self.cleaned_data['stock'] < 0:
            raise ValidationError("Can't have a negative initial stock")
        return self.cleaned_data


