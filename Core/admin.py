from django.contrib import admin
from typing import Any
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from Core.models import Tag, Category, Product, User, Client, Employee


class SiteAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'Employee':
            kwargs['queryset'] = User.objects.filter(is_employee_is=False). order_by('name')
        
        return super().formfield_for_manytomany(db_field, request, **kwargs)

# Register your models here.
admin.site.register(User)
admin.site.register(Employee, SiteAdmin)
admin.site.register(Client)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)
