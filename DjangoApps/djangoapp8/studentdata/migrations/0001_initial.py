# Generated by Django 3.2.6 on 2021-08-19 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
