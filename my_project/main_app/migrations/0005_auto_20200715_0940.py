# Generated by Django 3.0.3 on 2020-07-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200715_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address2',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=None, max_length=1024, verbose_name='Address'),
        ),
    ]
