from django.db import models

class TecnicaCirurgica(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tecninca cirurgica")

    class Meta:
        verbose_name = "Técninca cirúrgica"
        verbose_name_plural = "Técnincas cirúrgicas"

    def __str__(self) -> str:
        return f"{self.name}"