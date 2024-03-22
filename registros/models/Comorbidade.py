from django.db import models
from multiselectfield import MultiSelectField

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class Comorbidade(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = "Tipo de comorbidade"
        verbose_name_plural = "Tipos de comorbidades"

    def __str__(self) -> str:
        return f"{self.name}"