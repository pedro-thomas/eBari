from django.db import models

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

from registros.models import OpcoesFamilia
class HistoricoFamiliar(models.Model):
    patient = models.ForeignKey('pacientes.Paciente', verbose_name="Paciente", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    family_obesity = models.ManyToManyField(
        OpcoesFamilia,
        verbose_name="Obesidade na familia",
        related_name='family_obesity',
        blank=False
    )

    family_hypertension = models.ManyToManyField(
        OpcoesFamilia,
        verbose_name="Hipertensão na familia",
        related_name='family_hypertension',
        blank=False
    )

    family_diabetes = models.ManyToManyField(
        OpcoesFamilia,
        verbose_name="Diabetes na familia",
        related_name='family_diabetes',
        blank=False
    )

    family_coronary = models.ManyToManyField(
        OpcoesFamilia,
        verbose_name="Doença coronariana na familia",
        related_name='family_coronary',
        blank=False
    )

    family_avc = models.ManyToManyField(
        OpcoesFamilia,
        verbose_name="AVC na familia",
        related_name='family_avc',
        blank =False
    )
    family_cancer = models.ManyToManyField(
        OpcoesFamilia,
        verbose_name="Cancêr na familia",
        related_name='family_cancer',
        blank=False
    )

    class Meta:
        verbose_name = "Histórico Familiar"
        verbose_name_plural = "Históricos Familiares"