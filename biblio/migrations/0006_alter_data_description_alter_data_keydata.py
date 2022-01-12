# Generated by Django 4.0.1 on 2022-01-11 03:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0005_personne_alter_data_keydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='description',
            field=models.TextField(blank=True, default='Aucune description', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='data',
            name='keydata',
            field=models.UUIDField(default=uuid.UUID('ce2e5ba2-728e-11ec-8bb6-a0481cdcb140'), editable=False),
        ),
    ]