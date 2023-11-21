from django.contrib import admin
from Core.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import Tag, Category, Product, User, Client, Employee


class SiteAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field == 'Employee':
            kwargs['queryset'] = User.objects.filter(is_employee_is=False). order_by('name')
        
        return super().formfield_for_manytomany(db_field, request, **kwargs)

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
admin.site.register(Employee, SiteAdmin)
admin.site.register(Client)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)
