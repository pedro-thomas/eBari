from django import forms
from models.FormOperatorio import PreOperatorio, PosOperatorio

class PosOperatorioForm(forms.ModelForm):
    class Meta:
        model = PosOperatorio
        fields = '__all__'
        exclude = ['consulta']

class PosOperatorioForm(forms.ModelForm):
    class Meta:
        model = PreOperatorio
        fields = '__all__'
        exclude = ['consulta']