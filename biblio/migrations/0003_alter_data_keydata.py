# Generated by Django 4.0.1 on 2022-01-10 17:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0002_data_keydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='keydata',
            field=models.UUIDField(default=uuid.UUID('ad7608db-371b-461b-b4b1-93c928f82107')),
        ),
    ]
