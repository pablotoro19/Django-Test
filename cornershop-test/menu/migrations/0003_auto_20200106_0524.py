# Generated by Django 2.0.2 on 2020-01-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.AlterField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default='00d5e065da0a48e994fd8d079d53add5'),
        ),
    ]