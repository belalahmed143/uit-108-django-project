# Generated by Django 3.2.16 on 2023-01-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_alter_order_ordered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_order_amount',
            field=models.IntegerField(default=500),
        ),
    ]