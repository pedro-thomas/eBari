from django.db import models

# Opções de Locais de refeições: 'Casa','Trabalho','Restaurante','Escola/Faculdade

class LocalRefeicao(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Local de Refeição'
        verbose_name_plural = 'Locais de Refeições'

    def __str__(self) -> str:
        return f"{self.name}"
