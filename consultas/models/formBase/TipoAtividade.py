from django.db import models

# Opções de Tipo de Atividade:
# 1. Caminhada
# 2. Hidroginástica
# 3. Musculação
# 4. Dança
# 5. Outros (deixar espaço para ESCREVER)

class TipoAtividade(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Tipo de Atividade'
        verbose_name_plural = 'Tipo de Atividade'

    def __str__(self) -> str:
        return f"{self.name}"
