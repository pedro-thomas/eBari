# Generated by Django 5.0.1 on 2024-03-22 02:28

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comorbidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de comorbidade',
                'verbose_name_plural': 'Tipos de comorbidades',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
        ),
        migrations.CreateModel(
            name='Patologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Patologia',
                'verbose_name_plural': 'Patologias',
            },
        ),
        migrations.CreateModel(
            name='ProblemasGastricos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Problema gastrointestinal',
                'verbose_name_plural': 'Problemas gastrointestinais',
            },
        ),
        migrations.CreateModel(
            name='RegistroBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('pre_op', 'Pré-operatório'), ('pos_op', 'Pós-operatório')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Rémedio',
                'verbose_name_plural': 'Remédios',
            },
        ),
        migrations.CreateModel(
            name='TecnicaCirurgica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tecninca cirurgica')),
            ],
            options={
                'verbose_name': 'Técninca cirúrgica',
                'verbose_name_plural': 'Técnincas cirúrgicas',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('state', models.CharField(choices=[('MT', 'Mato Grosso'), ('TO', 'Tocantins'), ('GO', 'Goiás')], max_length=2, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'unique_together': {('name', 'state')},
            },
        ),
        migrations.CreateModel(
            name='HistoricoFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('family_obesity', multiselectfield.db.fields.MultiSelectField(choices=[('nao', 'Não'), ('pais', 'Pais'), ('avos', 'Avós'), ('tios', 'Tios'), ('irmaos', 'Irmãos')], max_length=25, verbose_name='Obesidade na familia')),
                ('family_hypertension', multiselectfield.db.fields.MultiSelectField(choices=[('nao', 'Não'), ('pais', 'Pais'), ('avos', 'Avós'), ('tios', 'Tios'), ('irmaos', 'Irmãos')], max_length=25, verbose_name='Hipertensão na familia')),
                ('family_diabetes', multiselectfield.db.fields.MultiSelectField(choices=[('nao', 'Não'), ('pais', 'Pais'), ('avos', 'Avós'), ('tios', 'Tios'), ('irmaos', 'Irmãos')], max_length=25, verbose_name='Diabetes na familia')),
                ('family_coronary', multiselectfield.db.fields.MultiSelectField(choices=[('nao', 'Não'), ('pais', 'Pais'), ('avos', 'Avós'), ('tios', 'Tios'), ('irmaos', 'Irmãos')], max_length=25, verbose_name='Doença coronariana na familia')),
                ('family_avc', multiselectfield.db.fields.MultiSelectField(choices=[('nao', 'Não'), ('pais', 'Pais'), ('avos', 'Avós'), ('tios', 'Tios'), ('irmaos', 'Irmãos')], max_length=25, verbose_name='AVC na familia')),
                ('family_cancer', multiselectfield.db.fields.MultiSelectField(choices=[('nao', 'Não'), ('pais', 'Pais'), ('avos', 'Avós'), ('tios', 'Tios'), ('irmaos', 'Irmãos')], max_length=25, verbose_name='Cancêr na familia')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Histórico Familiar',
                'verbose_name_plural': 'Históricos Familiares',
            },
        ),
    ]