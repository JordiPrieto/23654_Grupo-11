# Generated by Django 4.2.5 on 2023-11-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=15, null=True, unique=True, verbose_name='Tag'),
        ),
    ]
