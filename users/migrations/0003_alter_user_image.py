# Generated by Django 4.2.1 on 2023-11-22 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='users_images', verbose_name='Фото'),
        ),
    ]