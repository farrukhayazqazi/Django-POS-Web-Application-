# Generated by Django 3.0.3 on 2020-07-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20200725_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='productID',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.CharField(default='product', max_length=100),
        ),
    ]