from django.db import models

# Opções de Obesidade na Familia: 'Não', 'Pais', 'Avós', 'Tios', 'Irmãos'

class OpcoesFamilia(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Opcões Familiares'
        verbose_name_plural = 'Opcões Familiares'

    def __str__(self) -> str:
        return f"{self.name}"
