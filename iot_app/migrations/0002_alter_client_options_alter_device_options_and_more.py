# Generated by Django 4.2.5 on 2023-10-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'Device', 'verbose_name_plural': 'Devices'},
        ),
        migrations.AddField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Actif'),
        ),
        migrations.AddField(
            model_name='device',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='Est actif'),
        ),
    ]