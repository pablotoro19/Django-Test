# Generated by Django 2.0.2 on 2020-01-07 21:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.AddField(
            model_name='menu',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('3f653c77-9625-4552-9a78-d1047753ba1f')),
        ),
    ]
