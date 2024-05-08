from django.db import models

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class RegistroBase(models.Model):
    TYPE_CHOICES = (
        ('Pré-operatório', 'Pré-operatório'),
        ('Pós-operatório', 'Pós-operatório'),
    )

    type = models.CharField(max_length=15, choices=TYPE_CHOICES, null=True, blank=True)