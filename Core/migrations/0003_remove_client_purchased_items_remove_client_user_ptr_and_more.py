# Generated by Django 4.2.5 on 2023-11-20 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_alter_tag_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='purchased_items',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_tags',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]