from django import forms
from models.Consultas import Consulta

class ConsultasForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = 'patient', 'date', 'type', 'notes'