# Generated by Django 3.0.3 on 2020-07-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20200719_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='rate',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='takeorder',
            name='rate',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
