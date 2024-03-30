from django.db import models

class HorarioTrabalho(models.Model):
    name =  models.CharField(max_length=48,verbose_name="Horário")

    class Meta:
        verbose_name = "Horário de Trabalho"
        verbose_name_plural = "Horários de Trabalho"
        
    def __str__(self):
        return self.name
    