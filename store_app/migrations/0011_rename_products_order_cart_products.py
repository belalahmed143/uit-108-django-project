# Generated by Django 4.1.3 on 2022-12-12 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0010_cartproduct_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='cart_products',
        ),
    ]
