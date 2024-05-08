from django.db import models

# Opções de Tipo de motivo para não praticar Atividade:
# 1. Indisposição/preguiça
# 2. Falta de tempo
# 3. Vergonha
# 4. Outros (deixar espaço para ESCREVER)

class MotivoAtividade(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Motivo de Não Atividade'
        verbose_name_plural = 'Motivo de Não Atividade'

    def __str__(self) -> str:
        return f"{self.name}"
