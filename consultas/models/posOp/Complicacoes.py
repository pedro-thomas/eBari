from django.db import models

# Opções de Sintomas gastrointestinais pós-cirurgicos: 'Não possui','Vômitos','Constipação intestinal','Entalamento','Alopécia','Halitose','Flatulência','Diarreia','Síndrome de Dumping','Azia ou náuseas','Unha fraca ou quebradiça'    

class Complicacoes(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = 'Sintomas gastrointestinais pós-cirurgicos'
        verbose_name_plural = 'Sintomas gastrointestinais pós-cirurgicos'

    def __str__(self) -> str:
        return f"{self.name}"
