# Generated by Django 3.0.3 on 2020-07-15 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20200715_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='OrderID',
        ),
    ]
