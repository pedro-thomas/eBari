from django import forms
from models.Consultas import Consulta
from models.Exames import Exame

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = 'hemoglobina', 'hematocrito', 'hemacias', 'rdw', 'vcm', 'hcm', 'chcm', 'leucocitos', 'colesterol_total', 'hdl', 'ldl', 'vldl', 'triglicerideos', 'glicemia_de_jejum', 'albumina', 'ferritina', 'ferro_serico', 'insulina', 'vitamina_D', 'vitamina_B12', 'vitamina_B9', 'hemoglobina_glicada', 'homa_ir'