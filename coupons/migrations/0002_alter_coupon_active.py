# Generated by Django 3.2.13 on 2023-04-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
