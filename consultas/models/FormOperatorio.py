from typing import Any
from django.db import models
from pacientes.models import Paciente
from multiselectfield import MultiSelectField
from multiselectfield.utils import get_max_length

from consultas.models import Consultas
from registros.models import Comorbidade, ProblemasGastricos, Remedio, Medico, TecnicaCirurgica, Patologia

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class PosOperatorio(models.Model):
    consulta = models.OneToOneField(Consultas, on_delete=models.CASCADE, related_name='posop')

    surgery_date = models.DateField(
        verbose_name="Data da cirurgia",
        blank=False,
        null= False
    )

    PLAN_CHOICES = (
        ('SUS', 'SUS'),
        ('Plano de saúde / Particular', 'Plano de saúde / Particular'),
    )

    surgery_plan = models.CharField(
        max_length=255,
        choices = PLAN_CHOICES,
        verbose_name="Convênio da cirurgia",
        blank=False,
        null= False
    )

    surgery_local = models.CharField(
        max_length=255,
        verbose_name="Local da cirurgia",
        blank=False,
        null= False
    )

    doctors_name = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        blank=False,
        null= False,
        verbose_name="Médico responsável pela cirurgia",
    )

    surgery_technique = models.ForeignKey(
        TecnicaCirurgica, on_delete=models.CASCADE, 
        blank=False,
        null= False,
        verbose_name="Técninca ultilizada na cirurgia",
    )
    
    TIME_CHOICES = (
        ('nao realizou','Não realizou'),
        ('Menos de 6 meses', 'Menos de 6 meses'),
        ('Mais de 6 Meses', 'Mais de 6 Meses'),
    )

    psy_time = models.CharField(
        max_length=255,
        choices = TIME_CHOICES,
        verbose_name="Quanto tempo durou o acompanhamento psicológico",
        blank=False,
        null= False
    )

    psy_still = models.BooleanField(
        max_length=25,
        choices = SIM_NAO_CHOICES,
        verbose_name="Ainda faz acompanhamento psicológico",
        blank=False,
        null= False
    )

    NUTRI_CHOICES = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
        ('Só laudo', 'Só laudo'),
    )

    nutri = models.CharField(
        max_length=255,
        choices = NUTRI_CHOICES,
        verbose_name="Fez acompanhamento com nutricionista antes da cirurgia",
        blank=False,
        null= False
    )

    nutri_time = models.CharField(
        max_length=255,
        choices = TIME_CHOICES,
        verbose_name="Quanto tempo durou o acompanhamento com nutricionista",
        blank=False,
        null= False
    )
    
    med_use = models.ManyToManyField(
        Remedio,
        verbose_name="Qual medicamento consome atualmente",
    )

    med_stop = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Parou de tomar algum medicamento pós cirurgia",
        blank=False,
        null= False
    )

    stop_type= models.CharField( 
        max_length= 255,
        null=True, 
        blank=True, 
        verbose_name="Qual medicamento parou de tomar",
    )

    vit_consu = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Toma algum suplemento polivitaminico",
        blank=False,
        null= False
    )

    vit_type = models.CharField(
        max_length=255,
        verbose_name="Qual suplemento e posologia",
        null=True,
        blank= True
    )

    whey_consu = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Toma algum suplemento proteico",
        blank=False,
        null= False
    )

    whey_type = models.CharField(
        max_length=255,
        verbose_name="Qual suplemento e posologia",
        null=True,
        blank= True
    )

    current_comorbidities = models.ManyToManyField(
        Comorbidade,
        verbose_name="Comorbidades atuais",
        blank = False,
    )

    improved_comorb = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Comorbidades melhoraram pós cirurgia",
        blank=False,
        null= False
    )

    improved_type = models.CharField(
        max_length=255, null=True,
        blank=True, verbose_name="Quais comorbidades melhoraram?",
    )

    current_pathology = models.ManyToManyField(
        Patologia,
        blank=False, verbose_name="Patologias atuais",
    )

    COMPLICATIONS_CHOICES = (
        ('não possui','Não possui'),
        ('vomitos', 'Vômitos'),
        ('contipacao intestinal', 'Constipação intestinal'),
        ('entalamento', 'Entalamento'),
        ('alopecia', 'Alopécia'),
        ('halitose', 'Halitose'),
        ('flatulencia', 'Flatulência'),
        ('diarreia', 'Diarreia'),
        ('sindome de dumping', 'Síndrome de Dumping'),
        ('azia ou nauseas', 'Azia ou náuseas'),    
        ('uma fraca/quebradica ','Unha fraca ou quebradiça')    
    )

    complications = MultiSelectField(
        max_length = 255,
        choices = COMPLICATIONS_CHOICES,
        verbose_name = "Sintomas gastrointestinais pós-cirurgicos",
        blank=False,
        null= False
    )

    complications_obs = models.TextField(
        verbose_name="Observações",
        blank=True,
    )

    food_intolerance = models.BooleanField(
        choices= SIM_NAO_CHOICES,
        verbose_name="Apresentou intolerancia alimentar a algum alimento após a CB?",
        blank=False,
        null= False
    )

    food_type = models.CharField(
        max_length=255,
        verbose_name="Quais alimentos",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pós-Operatório'
        verbose_name_plural = 'Pós-Operatórios'

    def __str__(self):
        return f"Detalhes Pós-Op para {self.consulta}"
    
class PreOperatorio(models.Model):
    consulta = models.OneToOneField(Consultas, on_delete=models.CASCADE, related_name='preop')

    DIET_CHOICES = (
        ('0', '0 - Não fiz'),
        ('1', '1 - Dietas da moda'),
        ('2', '2 - Conta própria'),
        ('3', '3 - Reeducação Alimentar'),
        ('4', '4 - Shakes emagrecedores'),
        ('5', '5 - Medicamento (Prescrição médica)'),
        ('6', '6 - Automedicação (Sem prescrição médica)'),
        ('7', '7 - Plano alimentar (Prescrição medica. Qual médico?)'),
        ('8', '8 - Grupos de emgragrecimento (Com nutricionista)'),
        ('9', '9 - Grupos de emagrecimento (Sem nutricionista)'),
        ('10', '10 - Coach'),
        ('11', '11 - Outros (Descreva abaixo)'),
    )

    do_diet = models.IntegerField(
        choices= SIM_NAO_CHOICES,
        verbose_name="Fez algum tipo de dieta para perda de peso?",
        blank=False,
        null= False
    )

    DIET_ORIENTATION_CHOICES = (
        ('1', '1 - Eu mesmo(a)'),
        ('2', '2 - Nutricionista'),
        ('3', '3 - Médico'),
        ('4', '4 - Amigos/Familiares'),
        ('5', '5 - Coaching'),
        ('6', '6 - Outros'),
    )
    
    diet_orientation = MultiSelectField(
            verbose_name="Quem orientou a dieta?",
            choices=DIET_ORIENTATION_CHOICES,
            max_length=get_max_length(DIET_ORIENTATION_CHOICES, None),
            blank=True,
    )  

    weight_time = models.IntegerField(
        max_length=25,
        verbose_name="Há quanto tempo apresenta excesso de peso?",
        blank=False,
    )  

    WEIGHT_REASON_CHOICES = (
        ('Gestação', 'Gestação'),
        ('Genética', 'Genética'),
        ('Hábitos de vida', 'Hábitos de vida'),
        ('Patologia', 'Patologia'),
        ('Casamento', 'Casamento')
    )

    weight_reason = MultiSelectField(
        max_length=25,
        choices= WEIGHT_REASON_CHOICES,
        verbose_name="Causa do ganho de peso",
        blank=False,
    )

    obs = models.TextField(
            max_length=255,
            verbose_name="Observações",
            blank=True,
    )
    
    comorbidities_type = models.ManyToManyField(
        Comorbidade,
        verbose_name="Comorbidades",
        blank = False,
    )

    stomach_problems = models.ManyToManyField(
        ProblemasGastricos,
        blank=False,
        verbose_name="Problemas gastrointestinais",
    )
    med_consumption = models.ManyToManyField(
        Remedio,
        blank = False, 
        verbose_name="Consome medicamentos",
    )

    sup_consumption = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Consome algum suplemento alimentar",
        blank=False,
        null= False,
    )

    sup_type = models.CharField(
        max_length=255,
        verbose_name="Se sim, qual suplemento",
        blank=True,
    )

    bari_security= models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Está seguro em realizar a cirurgia?",
        blank=False,
        null= False
    )

    familly_support = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Familia apoia a cirurgia?",
        blank=False,
        null= False
    )

    FOOD_OP = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Muito pouco', 'Muito pouco'),
    )

    pos_cb_food = models.CharField(
        max_length=25,
        choices = FOOD_OP,
        verbose_name="Você sabe como será sua alimentação após a cirurgia",
        blank=False,
    )

    description = models.TextField(blank=True, verbose_name="Observações")

    PLAN_CHOICES = (
        ('SUS', 'SUS'),
        ('Plano de saúde / Particular', 'Plano de saúde / Particular'),
    )

    surgery_plan = models.CharField(
        max_length=255,
        choices = PLAN_CHOICES,
        verbose_name="Convênio da cirurgia",
        blank=False,
    )

    surgery_op = models.TextField(blank=False, verbose_name="Por que decidiu optar pela cirurgia bariatrica")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pré-Operatório'
        verbose_name_plural = 'Pré-Operatórios'

    def __str__(self):
        return f"Detalhes Pré-Op para {self.consulta}"
    
    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     self.validators[0] = MaxValueMultiFieldValidator(self.max_length)

    #     super().__init__(*args, **kwargs)