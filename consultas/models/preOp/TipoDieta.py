from django.db import models

# Opções de Tipo de dieta:
# '0 - Não fiz',
# '1 - Dietas da moda',
# '2 - Conta própria',
# '3 - Reeducação Alimentar c/ Nutricionista',
# '4 - Shakes emagrecedores',
# '5 - Medicamento (Prescrição médica)',
# '6 - Automedicação (Sem prescrição médica)',
# '7 - Plano alimentar (Prescrição medica. Qual médico?)',
# '8 - Grupos de emgragrecimento (Com nutricionista)',
# '9 - Grupos de emagrecimento (Sem nutricionista)',
# '10 - Coach',
# '11 - Outros (Descreva abaixo)'

class TipoDieta(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Tipo de dieta'
        verbose_name_plural = 'Tipo de dieta'

    def __str__(self) -> str:
        return f"{self.name}"
