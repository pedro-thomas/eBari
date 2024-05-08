from django.db import models

# Opções: 
# 1. HAS
# 2. DM
# 3. Pré diabetes
# 4. Resistencia a insulina
# 5. Doença ortopédica
# 6. Dislipidemia
# 7. Depressão
# 8. Ansiedade
# 9. Apnéia
# 10. Esteatose hepática
# 11. Hiperuricemia/gota
# 12. Histórico de câncer
# 13. Hipotiroidismo
# 14. Ovário policisticos
# 15. Doenças cardíacas
# 16. Outros (deixar espaço para escrever)

class Comorbidade(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        verbose_name = "Tipo de comorbidade"
        verbose_name_plural = "Tipos de comorbidades"

    def __str__(self) -> str:
        return f"{self.name}"