# Generated by Django 5.0.7 on 2024-08-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30)),
                ('c_email', models.CharField(max_length=30)),
                ('c_contact', models.CharField(max_length=30)),
                ('c_age', models.IntegerField()),
                ('c_address', models.TextField(max_length=30)),
            ],
        ),
    ]
