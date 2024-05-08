from django.db import models

class Remedio(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = "Rémedio"
        verbose_name_plural = "Remédios"

    def __str__(self) -> str:
        return f"{self.name}"