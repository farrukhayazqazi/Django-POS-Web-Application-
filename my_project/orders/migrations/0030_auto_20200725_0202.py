# Generated by Django 3.0.3 on 2020-07-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_auto_20200725_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='productID',
            field=models.CharField(default='product', max_length=100),
        ),
    ]
