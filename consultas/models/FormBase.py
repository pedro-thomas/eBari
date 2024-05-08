from django.db import models
from consultas.models import Consultas, LocalRefeicao, TipoAlcool, QuemPrepara

SIM_NAO_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)

class FormBase(models.Model):
    consulta = models.OneToOneField(Consultas, on_delete=models.CASCADE, related_name='form_base')

    meal_place = models.ManyToManyField(LocalRefeicao, verbose_name="Onde realiza refeições", blank=False)

    tv_eating = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name = "Realiza as refeições vendo alguma tela (TV, Celular, Computador)",
        blank=False,
        null= False
    )

    chews_food = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name = "Mastiga bem os alimentos",
        blank=False,
        null= False
    )

    fist_food = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name = "É o(a) primeiro a terminar de comer?",
        blank=False,
        null= False
    )

    food_aversions = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name ="Aversões alimentares",
        blank=False,
    )

    aversions_type = models.CharField(
        max_length = 255,
        verbose_name = "Quais aversões",
        blank=True,
    )

    food_preferences = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Preferências alimentares",
        blank=False,
        null= False
    )

    preferences_type = models.CharField(
        max_length=255,
        verbose_name="Quais preferências",
        blank=True,
    )

    food_compulsion = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Compulsões alimentares",
        blank=False,
        null= False
    )

    compulsion_type = models.CharField(
        max_length=255,
        verbose_name="Qual alimento e motivo",
        blank=True,
    )

    food_intolerance = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Intolerância alimentar",
        blank=False,
        null= False
    )

    intolerance_type = models.CharField(
        max_length=255,
        verbose_name="Quais alimentos",
        blank=True,
    )

    food_allergy = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Alergia alimentar",
        blank=False,
        null= False
    )

    allergy_type = models.CharField(
        max_length=255,
        verbose_name="Quais alimentos",
        blank=True,
    )

    WATER_CHOICES = (
        ('menos de 500ml', 'Menos de 500ml'),
        ('500ml a 1l', '500ml a 1L'),
        ('1l a 2l', '1L a 2L'),
        ('2l ou mais', '2L ou mais'),
    )

    water_consumption = models.CharField(
        max_length = 25,
        choices = WATER_CHOICES,
        verbose_name = "Consumo de água",
        blank=False,
    )

    ECAP_CHOICES = (
        ('Sem CAP', 'Sem CAP'),
        ('CAP moderada', 'CAP moderada'),
        ('CAP grave', 'CAP grave'),
    )
    
    ecap = models.CharField(
        max_length = 25,
        choices = ECAP_CHOICES,
        verbose_name = "Escala de compulsão alimentar",
        blank=False,       
    )

    observation = models.TextField(blank=True, verbose_name="Observações")

    physical_activity = models.BooleanField(
        choices= SIM_NAO_CHOICES,
        verbose_name="Pratica atividade fisica",
        blank=False,
        null= False
    )

    activity_type = models.CharField(
        max_length=255,
        verbose_name="Qual atividade?/Se não qual o motivo?",
        blank=True,
    )

    ACTIVITY_FREQUENCY_CHOICES = (
        ('nao pratica', 'Não pratica'),
        ('1 vez por semana', '1 vez por semana'),
        ('2 vezes por semana', '2 vezes por semana'),
        ('3 vezes por semana', '3 vezes por semana'),
        ('4 vezes por semana', '4 vezes por semana'),
        ('5 vezes por semana', '5 ou mais vezes por semana'),
    )

    activity_frequency = models.CharField(
        max_length=25,
        choices= ACTIVITY_FREQUENCY_CHOICES,
        verbose_name="Frequencia das atividades",
        blank=True,
    )

    ACTIVITY_DURATION_CHOICES = (
        ('nao pratica', 'Não pratica'),
        ('30 minutos', '30 minutos'),
        ('1 hora', '1 hora'),
        ('mais de uma hora', 'mais de uma hora'),
    )

    activity_duration = models.CharField(
        max_length=25,
        choices= ACTIVITY_DURATION_CHOICES,
        verbose_name="Duração das atividades",
        blank=True,
    )

    activity_like = models.BooleanField(
        choices= SIM_NAO_CHOICES,
        verbose_name="Gosta de fazer atividades fisicas",
        blank=False,
        null= False
    )

    like_activity_type = models.CharField(
        max_length=255,
        verbose_name="Qual atividade",
        blank=True,
    )

    SMOKER_CHOICES = (
        ('nunca fumou','Nunca fumou'),
        ('ex-fumante','Ex-fumante'),
        ('1 a 4 cigarros', '1 a 4 cigarros'),
        ('5 a 10 cigarros', '5 a 10 cigarros'),
        ('Mais de 10 cigarros', 'Mais de 10 cigarros'),
    )

    smoker= models.CharField(
        max_length=25,
        choices = SMOKER_CHOICES,
        verbose_name="Consumo de cigarro",
        blank=False,
        null= False
    )

    ALC_FREQ_CHOICES = (
        ('Raro/nunca', 'Raro/nunca'),
        ('1 vez por mês', '1 vez por mês'),
        ('2 vezes por mês', '2 vezes por mês'),
        ('1 vez por semana', '1 vez por semana'),
        ('2 vezes por semana', '2 vezes por semana'),
        ('3 vezes por semana', '3 vezes por semana'),
        ('Mais de 3 vezes por semana', 'Mais de 3 vezes por semana'),
        ('Todo dia', 'Todo dia'),
    )

    alcoholic = models.CharField(
        max_length=255,
        choices = ALC_FREQ_CHOICES,
        verbose_name="Consumo de bebida alcoolica",
        blank=False,
        null= False
    )
    
    alcoholic_type = models.ManyToManyField(
        TipoAlcool,
        verbose_name="Qual bebida",
        blank=True
    )

    drink_qtd = models.FloatField(
        verbose_name="Quantidade (ml)",
        null=True,
    )

    sleep_time = models.IntegerField(
        verbose_name="Horas de sono",
        null=True,
    )

    sleep_somnolence = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Sonolencia durante o dia",
        blank=False,
        null= False
    )

    sleep_wake = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Acorda durante a noite?",
        blank=False,
        null= False
    )

    wake_rested = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Acorda descansado?",
        blank=False,
        null= False
    )

    current_weight = models.FloatField(
        verbose_name="Peso atual",
        null=True,
    )

    stature = models.FloatField(
        verbose_name="Estatura (m)",
        null=True,
    )

    imc = models.FloatField(
        verbose_name="IMC (Kg/m²)",
        null=True,
    )

    waist = models.FloatField(
        verbose_name="Cintura (cm)",
        null=True,
    )

    hip = models.FloatField(
        verbose_name="Quadril (cm)",
        null=True,
    )

    neck = models.FloatField(
        verbose_name="Pescoço (cm)",
        null=True,
    )
    
    weight_excess = models.FloatField(
        verbose_name="Excesso de peso (atual)",
        null=True,
        blank= True
    )

    accumulated_weight_loss = models.FloatField(
        verbose_name="Perda de peso (kg)",
        null=True,
        blank= True
    )

    nutri_state = models.CharField(
        max_length=255,
        verbose_name="Estado nutricional",
        null=True,
    )
    
    def goal_weight(self):
        value = (self.stature*self.stature*29.9)
        return ("{:.2f}".format(value))
    goal_weight.short_description= 'Peso meta'

    def ideal_weight(self):
        value = (self.stature*self.stature*24.9)
        return ("{:.2f}".format(value))
    ideal_weight.short_description= 'Peso ideal'

    def imc(self):
        value = (self.current_weight)/(self.stature*self.stature)
        return ("{:.2f}".format(value))
    imc.short_description= 'IMC'

    breakfast_hour = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Hora do café da manhã"
    )

    breakfast_location = models.CharField(
        blank=True,
        max_length=30,
        verbose_name="Local do café da manhã"
    )

    breakfast_food = models.TextField(
        blank=True,
        verbose_name="Alimentos do café da manhã"
    )

    breakfast_food_quantities = models.TextField(
        blank=True,
        verbose_name="Quantidades de alimentos do café da manhã"
    )

    snack_after_breakfast_hour = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Hora da colação"
    )

    snack_after_breakfast_location = models.CharField(
        blank=True,
        max_length=30,
        verbose_name="Local da colação"
    )

    snack_after_breakfast_food = models.TextField(
        blank=True,
        verbose_name="Alimentos da colação"
    )

    snack_after_breakfast_food_quantities = models.TextField(
        blank=True,
        verbose_name="Quantidades de alimentos da colação"
    )

    lunch_hour = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Hora do almoço"
    )

    lunch_location = models.CharField(
        blank=True,
        max_length=30,
        verbose_name="Local do almoço"
    )

    lunch_food = models.TextField(
        blank=True,
        verbose_name="Alimentos do almoço"
    )

    lunch_food_quantities = models.TextField(
        blank=True,
        verbose_name="Quantidades de alimentos do almoço"
    )

    snack_hour = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Hora do lanche da tarde"
    )

    snack_location = models.CharField(
        blank=True,
        max_length=30,
        verbose_name="Local do lanche da tarde"
    )

    snack_food = models.TextField(
        blank=True,
        verbose_name="Alimentos do lanche da tarde"
    )

    snack_food_quantities = models.TextField(
        blank=True,
        verbose_name="Quantidades de alimentos do lanche da tarde"
    )

    dinner_hour = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Hora do jantar"
    )

    dinner_location = models.CharField(
        blank=True,
        max_length=30,
        verbose_name="Local do jantar"
    )

    dinner_food = models.TextField(
        blank=True,
        verbose_name="Alimentos do jantar"
    )

    dinner_food_quantities = models.TextField(
        blank=True,
        verbose_name="Quantidades de alimentos do jantar"
    )

    observation = models.TextField(blank=True, verbose_name="Observação")

    wake_consumption = models.BooleanField(
        choices = SIM_NAO_CHOICES,
        verbose_name="Acorda a noite pra comer",
        blank=False,
        null= False
    )

    FAT_TYPE_CHOICES = (
    ('Banha de porco', 'Banha de porco'),
    ('Vegetal', 'Vegetal'),
    ('Ambas', 'Ambas'),
    )

    fat_type = models.CharField(
        max_length=25,
        choices = FAT_TYPE_CHOICES,
        verbose_name="Tipo de gordura usada para a preparação da comida",
        blank=False,
    )

    fat_quant = models.CharField(
        max_length=25,
        verbose_name="Quantidade de gordura gasta por mês",
        blank=True,
    )

    who_prepares = models.ManyToManyField(
        QuemPrepara,
        verbose_name="Quem prepara as refeições",
        blank=False,
    )

    WHAT_SWEET = (
    ('Açúcar', 'Açúcar'),
    ('Adoçante', 'Adoçante'),
    )

    how_sweet = models.CharField(
        max_length=255,
        choices = WHAT_SWEET,
        verbose_name="Como adoça suas refeições?",
        blank=False,
    )

    sweet_type = models.CharField(
        max_length=255,
        verbose_name="Qual o tipo?",
        blank=True,
    )

    chewing_time = models.CharField(
        max_length=255,
        verbose_name="Tempo gasto na mastigação das refeições", 
        blank=False,
    )

    class Meta:
        verbose_name = 'Formulário Base'
        verbose_name_plural = 'Formulários Bases'

    def __str__(self):
        return f"Consulta de {self.paciente.full_name} em {Pacientete}"

    soap_s = models.TextField(blank=True, verbose_name="S (Subjetivo)")
    soap_o = models.TextField(blank=True, verbose_name="O (Objetivo)")
    soap_a = models.TextField(blank=True, verbose_name="A (Avaliação)")
    soap_p = models.TextField(blank=True, verbose_name="P (Plano)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)