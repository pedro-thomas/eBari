from django.db import models
from ...pacientes.models import Paciente
from multiselectfield import MultiSelectField

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class Cidade(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    STATE_CHOICES = (
        ('MT', 'Mato Grosso'),
        ('TO', 'Tocantins'),
        ('GO', 'Goiás'),
    )
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        verbose_name="Estado"
    )

    class Meta:
        unique_together = (
            'name',
            'state',
        )

        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self) -> str:
        return f"{self.name}/{self.state}"