# Generated by Django 3.2.6 on 2021-08-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='percentage',
            field=models.FloatField(default=0.0),
        ),
    ]