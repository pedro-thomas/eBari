from django.db import models

# Opções de Quem prepara as refeições: 'Você','Funcionária','Parente','Restaurante', 'Delivery/Marmitex'

class QuemPrepara(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Quem prepara as refeições'
        verbose_name_plural = 'Quem prepara as refeições'

    def __str__(self) -> str:
        return f"{self.name}"
