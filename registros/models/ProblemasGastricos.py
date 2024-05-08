from django.db import models
# Opções:
# 1. Azia
# 2. Gastrite
# 3. Ulcera
# 4. Constipação Intestinal
# 5. Diarreia
# 6. Refluxo
class ProblemasGastricos(models.Model):

    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = "Problema gastrointestinal"
        verbose_name_plural = "Problemas gastrointestinais"

    def __str__(self) -> str:
        return f"{self.name}"