# Generated by Django 5.0.7 on 2024-08-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseapp', '0005_alter_property_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(default='unknown', max_length=30),
        ),
    ]