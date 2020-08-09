# Generated by Django 3.0.3 on 2020-07-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_order_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='not paid', max_length=10),
        ),
    ]