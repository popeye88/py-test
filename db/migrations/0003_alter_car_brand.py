# Generated by Django 5.1.1 on 2024-09-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0002_alter_car_creation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="brand",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
