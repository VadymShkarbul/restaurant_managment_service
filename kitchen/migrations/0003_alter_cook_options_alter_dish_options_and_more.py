# Generated by Django 4.1.3 on 2022-11-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"verbose_name": "cook", "verbose_name_plural": "cooks"},
        ),
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name": "dish", "verbose_name_plural": "dishes"},
        ),
        migrations.AlterModelOptions(
            name="dishtype",
            options={
                "verbose_name": "dish type",
                "verbose_name_plural": "dishes types",
            },
        ),
        migrations.AlterField(
            model_name="dish",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
