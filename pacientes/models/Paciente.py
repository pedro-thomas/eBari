from django.db import models
from multiselectfield import MultiSelectField
from datetime import date

from registros.models import Cidade

class Paciente(models.Model):

    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")

    full_name = models.CharField(max_length=255, verbose_name="Nome Completo", null=False, blank=False,)

    birth_date = models.DateField(verbose_name="Data de Nascimento",null=False,blank=False,)

    GENDER_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Sexo",null=False,blank=False,)

    ocupation = models.CharField(max_length=255,verbose_name="Ocupação",null=False,blank=False,)

    WORK_HOURS_CHOICES = [
        ('morning', 'Manhã'),
        ('afternoon', 'Tarde'),
        ('evening', 'Noite'),
    ]

    work_hours = MultiSelectField(max_length=10,choices= WORK_HOURS_CHOICES,verbose_name="Horário de Trabalho")

    cellphone_number = models.CharField(max_length=20, verbose_name="Telefone Celular",null=True,blank= True)

    email = models.EmailField(null=True,blank=True)

    address_city = models.ForeignKey(Cidade, verbose_name="Cidade", on_delete=models.CASCADE,null=False,blank=False)

    address_home = models.CharField(max_length=150,null=False,blank=False,verbose_name="Endereço")

    HOUSING_TYPE_CHOICES = (
        ('sem renda', 'Sem renda'),
        ('1 a 2', '1 a 2'),
        ('2 a 4', '2 a 4'),
        ('4 a 10', '4 a 10'),
        ('10 a 20', '10 a 20'),
        ('20 ou mais', '20 ou mais'),
    )

    income_family= models.CharField(max_length=25,choices=HOUSING_TYPE_CHOICES,verbose_name="Renda Familiar (em salarios minimos)",null=False,blank=False,)

    HOUSING_TYPE_CHOICES = (
        ('própria', 'Própria'),
        ('alugada', 'Alugada'),
        ('cedida', 'Cedida'),
    )

    housing_type = models.CharField(max_length=25,choices=HOUSING_TYPE_CHOICES,verbose_name="Tipo de moradia",null=False,blank=False,)

    residents_number = models.PositiveSmallIntegerField(null=False,blank=False, verbose_name="Quantidade de moradores")

    offspring_number = models.PositiveSmallIntegerField(null=False,blank=False, verbose_name="Quantidade de filhos")

    EDUCATION_CHOICES = (
        ('analfabeto/analfabeto-funcional', 'Analfabeto/Analfabeto Funcional'),
        ('ensino-fundamental-incompleto', 'Ensino Fundamental Incompleto'),
        ('ensino-fundamental-completo', 'Ensino Fundamental Completo'),
        ('ensino-médio-incompleto', 'Ensino Médio Incompleto'),
        ('ensino-médio-completo', 'Ensino Médio Completo'),
        ('ensino-superior-incompleto', 'Ensino Superior Incompleto'),
        ('ensino-superior-completo', 'Ensino Superior Completo'),
    )
    education = models.CharField(max_length=50,choices=EDUCATION_CHOICES,verbose_name="Escolaridade",null=False,blank=False,)

    SKIN_CHOICES = (
        ('branca', 'Branca'),
        ('preta', 'Preta'),
        ('amarela', 'Amarela'),
        ('parda', 'Parda'),
        ('indigena', 'Indigena'),
    )

    skin = models.CharField(max_length=25,choices= SKIN_CHOICES,verbose_name="Pele",null=False,blank=False,)

    CIVIL_STATE_CHOICES = (
        ('solteiro', 'Solteiro'),
        ('casado/amasiado', 'Casado/Amasiado'),
        ('separado/divorciado', 'Separado/Divorciado'),
        ('viúvo', 'Viúvo'),
    )

    civil_state = models.CharField(max_length=50,choices=CIVIL_STATE_CHOICES,verbose_name="Estado civil",null=False,blank=False)

    
    REASON_CHOICES = (
        ('acompanhamento nutricional', 'Acompanhamento nutricional'),
        ('laudo nutricional', 'Laudo nutricional'),
        ('acompanhamento e laudo nutricional', 'Acompanhamento e Laudo nutricional'),
    )

    reason_consultation = models.CharField(max_length=50,choices=REASON_CHOICES,verbose_name="Motivo da consulta",null=False,blank=False)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f'{self.full_name}'
    
    def age(self):
        today = date.today()
        born = self.birth_date
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
  
    age.short_description = 'Idade'
    age.admin_order_field = 'birth_date'
