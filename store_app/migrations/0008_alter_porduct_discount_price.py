# Generated by Django 4.1.3 on 2022-12-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0007_porduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porduct',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
