# Generated by Django 5.1.1 on 2024-09-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0004_alter_car_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=models.TextField(default="Bla bla bla"),
        ),
    ]
