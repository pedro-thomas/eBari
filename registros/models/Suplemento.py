from django.db import models

class Suplemento(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = "Suplementos"
        verbose_name_plural = "Suplementos"

    def __str__(self) -> str:
        return f"{self.name}"