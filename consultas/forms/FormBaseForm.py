from django import forms
from models.FormBase import FormBase
from models.Consultas import Consulta

class FormBaseForm(forms.ModelForm):
    class Meta:
        model = FormBase
        fields = '__all__'
        exclude = ['consulta']