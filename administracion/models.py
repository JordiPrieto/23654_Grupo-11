from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=15, verbose_name='Tag', unique=True, null=True )
    active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.tag_name


class Category(models.Model):
    category_name = models.CharField(max_length=30, verbose_name="Category", unique=True)
    category_tags = models.ManyToManyField(Tag, verbose_name='Tag')
    active = models.BooleanField(default=True, verbose_name="Active")
    def __str__(self) -> str:
        return self.category_name


class Product(models.Model):
    prod_name = models.CharField(max_length=45, verbose_name="Product Name", unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)
    product_tags = models.ManyToManyField(Tag, verbose_name='Tags')
    stock = models.IntegerField(verbose_name="Stock", default=0)
    price = models.FloatField(verbose_name="Price", default=0)
    visible = models.BooleanField(verbose_name="Visible", default=False)
    active = models.BooleanField(default=True, verbose_name="Active")
    description = models.CharField(max_length=300, verbose_name='Description', null=True, blank=True)
    # image = models.URLField(verbose_name="image", null=True)
    image = models.ImageField(verbose_name="image:",upload_to="products_img",null=True)

    def __str__(self) -> str:
        return self.prod_name
    

class User(models.Model):
    username = models.CharField(max_length=15, verbose_name="Username", unique=True)
    first_name = models.CharField(max_length=15, verbose_name='First Name', null=False)
    last_name = models.CharField(max_length=15, verbose_name='Last Name', null=False)
    email = models.EmailField(max_length=45, verbose_name='Email', unique=True)
    active = models.BooleanField(default=True, verbose_name="Active")
    
    def __str__(self) -> str:
        return self.username


class Client(User):
    phone = models.CharField(max_length=20, verbose_name='Phone number', null=True)
    address_1 = models.CharField(max_length=20, verbose_name='Address 1', null=True)
    address_2 = models.CharField(max_length=20, verbose_name='Address 2', null=True)
    creation_date = models.DateField(verbose_name='Joined on')
    last_purchase_date = models.DateField(verbose_name='Last purchased on', null=True)
    purchased_items = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Purchased products', null=True)


class Employee(User):
    employee_number = models.IntegerField(verbose_name='Employee number', unique=True)
    phone_ext = models.IntegerField(verbose_name='Extension name', null=True)

