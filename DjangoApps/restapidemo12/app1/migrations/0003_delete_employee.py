# Generated by Django 3.2.7 on 2021-10-06 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_employee'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]