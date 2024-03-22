from django.db import models
from pacientes.models import Paciente

class Contato(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    contact_name =  models.CharField(
        max_length=48,
        verbose_name="Nome do contato"
    )
    description = models.CharField(
        max_length=30,
        verbose_name="Descrição"
    )
    cellphone_number = models.CharField(
        max_length=20,
        verbose_name="Telefone Celular"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
