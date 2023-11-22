from django.contrib import admin
from Core.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import Tag, Category, Product, User, Client, Employee



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'direccion')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'direccion'),
        }),
    )

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)
