# Generated by Django 4.1.3 on 2022-11-13 08:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_alter_cook_options_alter_dish_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cook',
            options={'ordering': ['username'], 'verbose_name': 'cook', 'verbose_name_plural': 'cooks'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['name'], 'verbose_name': 'dish', 'verbose_name_plural': 'dishes'},
        ),
        migrations.AlterModelOptions(
            name='dishtype',
            options={'ordering': ['name'], 'verbose_name': 'dish type', 'verbose_name_plural': 'dishes types'},
        ),
        migrations.AlterField(
            model_name='dish',
            name='cooks',
            field=models.ManyToManyField(related_name='dishes', to=settings.AUTH_USER_MODEL),
        ),
    ]