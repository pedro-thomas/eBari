from django.db import models
from pacientes.models import Paciente
from multiselectfield import MultiSelectField

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class Remedio(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = "Rémedio"
        verbose_name_plural = "Remédios"

    def __str__(self) -> str:
        return f"{self.name}"