# Generated by Django 4.0.6 on 2022-07-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_shops_img_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shops',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
