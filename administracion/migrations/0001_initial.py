# Generated by Django 4.2.5 on 2023-11-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True, verbose_name='Category')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=15, null=True, unique=True, verbose_name='Tag')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=15, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=45, unique=True, verbose_name='Email')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.user')),
                ('employee_number', models.IntegerField(unique=True, verbose_name='Employee number')),
                ('phone_ext', models.IntegerField(null=True, verbose_name='Extension name')),
            ],
            bases=('administracion.user',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=45, unique=True, verbose_name='Product Name')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('visible', models.BooleanField(default=False, verbose_name='Visible')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='Description')),
                ('image', models.ImageField(null=True, upload_to='products_img', verbose_name='image:')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.category')),
                ('product_tags', models.ManyToManyField(to='administracion.tag', verbose_name='Tags')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='category_tags',
            field=models.ManyToManyField(to='administracion.tag', verbose_name='Tag'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.user')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Phone number')),
                ('address_1', models.CharField(max_length=20, null=True, verbose_name='Address 1')),
                ('address_2', models.CharField(max_length=20, null=True, verbose_name='Address 2')),
                ('creation_date', models.DateField(verbose_name='Joined on')),
                ('last_purchase_date', models.DateField(null=True, verbose_name='Last purchased on')),
                ('purchased_items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.product', verbose_name='Purchased products')),
            ],
            bases=('administracion.user',),
        ),
    ]