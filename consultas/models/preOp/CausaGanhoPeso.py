from django.db import models

# Opções de Causa de ganho de peso: 'Gestação','Genética','Hábitos de vida','Patologia','Casamento'

class CausaGanhoPeso(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Causa do ganho de peso'
        verbose_name_plural = 'Causa do ganho de peso'

    def __str__(self) -> str:
        return f"{self.name}"
