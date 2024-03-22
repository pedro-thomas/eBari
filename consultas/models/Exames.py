from django.db import models
from pacientes.models import Paciente
from multiselectfield import MultiSelectField
from consultas.models.Consultas import Consultas

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class Exames(models.Model):
    consulta = models.OneToOneField(Consultas, on_delete=models.CASCADE, related_name='exams')
    has_exam = models.BooleanField(default=False)

    hemoglobina = models.CharField(max_length=20, blank=True)
    hematocrito = models.CharField(max_length=20, blank=True)
    hemacias = models.CharField(max_length=20, blank=True)
    rdw = models.CharField(max_length=20, blank=True)
    vcm = models.CharField(max_length=20, blank=True)
    hcm = models.CharField(max_length=20, blank=True)
    chcm = models.CharField(max_length=20, blank=True)
    leucocitos = models.CharField(max_length=20, blank=True)
    colesterol_total = models.CharField(max_length=20, blank=True)
    hdl = models.CharField(max_length=20, blank=True)
    ldl = models.CharField(max_length=20, blank=True)
    vldl = models.CharField(max_length=20, blank=True)
    triglicerideos = models.CharField(max_length=20, blank=True)
    glicemia_de_jejum = models.CharField(max_length=20, blank=True)
    albumina = models.CharField(max_length=20, blank=True)
    ferritina = models.CharField(max_length=20, blank=True)
    ferro_serico = models.CharField(max_length=20, blank=True)
    insulina = models.CharField(max_length=20, blank=True)
    vitamina_D = models.CharField(max_length=20, blank=True)
    vitamina_B12 = models.CharField(max_length=20, blank=True)
    vitamina_B9 = models.CharField(max_length=20, blank=True)
    hemoglobina_glicada = models.CharField(max_length=20, blank=True)
    homa_ir = models.CharField(max_length=20, blank=True)