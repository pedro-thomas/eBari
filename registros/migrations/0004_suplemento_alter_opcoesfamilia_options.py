# Generated by Django 5.0.3 on 2024-05-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_opcoesfamilia_remove_historicofamiliar_family_avc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suplemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Suplementos',
                'verbose_name_plural': 'Suplementos',
            },
        ),
        migrations.AlterModelOptions(
            name='opcoesfamilia',
            options={'verbose_name': 'Opcões Familiares', 'verbose_name_plural': 'Opcões Familiares'},
        ),
    ]
