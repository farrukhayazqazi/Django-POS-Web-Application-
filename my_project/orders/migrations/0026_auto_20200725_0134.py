# Generated by Django 3.0.3 on 2020-07-25 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20200725_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product',
            new_name='productID',
        ),
    ]
