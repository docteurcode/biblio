# Generated by Django 4.0.1 on 2022-01-11 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0006_alter_data_description_alter_data_keydata'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='nombre_de_lecture',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='keydata',
            field=models.UUIDField(editable=False),
        ),
    ]