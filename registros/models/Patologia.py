from django.db import models
from pacientes.models import Paciente
from multiselectfield import MultiSelectField

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class Patologia(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = "Patologia"
        verbose_name_plural = "Patologias"

    def __str__(self) -> str:
        return f"{self.name}"