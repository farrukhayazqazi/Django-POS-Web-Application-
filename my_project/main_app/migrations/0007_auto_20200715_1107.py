# Generated by Django 3.0.3 on 2020-07-15 18:07

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200715_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
