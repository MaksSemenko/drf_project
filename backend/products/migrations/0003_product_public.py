# Generated by Django 4.0.10 on 2023-04-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
