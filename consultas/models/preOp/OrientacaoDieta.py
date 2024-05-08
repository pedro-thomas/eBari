from django.db import models

# Opções de Quem Orientou a dieta: '1 - Eu mesmo(a)','2 - Nutricionista','3 - Médico','4 - Amigos/Familiares','5 - Coaching','6 - Outros'

class OrientacaoDieta(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Quem orientou a dieta?'
        verbose_name_plural = 'Quem orientou a dieta?'

    def __str__(self) -> str:
        return f"{self.name}"
