# Generated by Django 4.0.1 on 2022-01-10 09:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='keydata',
            field=models.UUIDField(default=uuid.UUID('48354b75-1f81-448e-a6cc-04a56ddc03bc')),
        ),
    ]
