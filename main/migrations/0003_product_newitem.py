# Generated by Django 4.2.5 on 2023-10-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='newItem',
            field=models.BooleanField(default=True),
        ),
    ]