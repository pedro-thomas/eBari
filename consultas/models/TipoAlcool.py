from django.db import models

# Opções de Tipos de Álcool: 'Cerveja','Vinho','Destilado / Cachaça','Outros'

class TipoAlcool(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Tipo de bebida Alcoólica'
        verbose_name_plural = 'Tipos de bebidas Alcoólicas'

    def __str__(self) -> str:
        return f"{self.name}"
