from django.db import models

from pacientes.models import Paciente

from multiselectfield import MultiSelectField

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class HistoricoFamiliar(models.Model):
    patient = models.ForeignKey('pacientes.Paciente', verbose_name="Paciente", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    FAMILY_CHOICES = (
        ('nao','Não'),
        ('pais', 'Pais'),
        ('avos', 'Avós'),
        ('tios', 'Tios'),
        ('irmaos', 'Irmãos'),
    )

    family_obesity = MultiSelectField(
        max_length= 25,
        choices= FAMILY_CHOICES,
        verbose_name="Obesidade na familia",
        blank=False,
        null= False
    )

    family_hypertension = MultiSelectField(
        max_length= 25,
        choices= FAMILY_CHOICES,
        verbose_name="Hipertensão na familia",
        blank=False,
        null= False
    )

    family_diabetes = MultiSelectField(
        max_length= 25,
        choices= FAMILY_CHOICES,
        verbose_name="Diabetes na familia",
        blank=False,
        null= False
    )

    family_coronary = MultiSelectField(
        max_length= 25,
        choices= FAMILY_CHOICES,
        verbose_name="Doença coronariana na familia",
        blank=False,
        null= False
    )


    family_avc = MultiSelectField(
        max_length= 25,
        choices = FAMILY_CHOICES,
        verbose_name="AVC na familia",
        blank =False,
        null = False
    )
    family_cancer = MultiSelectField (
        max_length= 25,
        choices= FAMILY_CHOICES,
        verbose_name="Cancêr na familia",
        blank=False,
        null= False
    )

    class Meta:
        verbose_name = "Histórico Familiar"
        verbose_name_plural = "Históricos Familiares"