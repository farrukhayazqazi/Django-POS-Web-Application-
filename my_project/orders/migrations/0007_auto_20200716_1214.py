# Generated by Django 3.0.3 on 2020-07-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200716_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='net_amount',
            field=models.IntegerField(default=0),
        ),
    ]