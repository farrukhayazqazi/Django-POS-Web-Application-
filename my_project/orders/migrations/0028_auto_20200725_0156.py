# Generated by Django 3.0.3 on 2020-07-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20200725_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='OrderID',
            field=models.IntegerField(null=True),
        ),
    ]
