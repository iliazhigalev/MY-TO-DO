# Generated by Django 4.2.1 on 2023-11-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]