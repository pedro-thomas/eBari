from django.db import models
from pacientes.models import Paciente
from multiselectfield import MultiSelectField
from registers.models import ComorbiditieType, GastProblem, Medicine, Doctor, Technique, CurrentPathology

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    date = models.DateField(verbose_name="Data da Consulta")
    type = models.CharField(max_length=20, choices=(('pre_op', 'PreOp'), ('pos_op', 'PosOp')), verbose_name="Tipo")
    notes = models.TextField(null=True, blank=True, verbose_name="Notas Adicionais")
      
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.paciente.full_name} - {self.created_at}"
