from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from pacientes.models import Paciente
from django.db.models import Q
from .forms import PacienteForm

class IndexView (TemplateView):
    template_name = "pacientes/home.html"

@login_required
def main_dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def list_pacientes(request):
    query = request.GET.get('search')
    if query:
        pacientes = Paciente.objects.filter(Q(full_name__icontains=query) | Q(cpf__icontains=query))
    else:
        pacientes = Paciente.objects.all()

    return render(request, 'list_pacientes.html', {'pacientes': pacientes})

@login_required   
def add_Paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pacientes')
    else:
        form = PacienteForm()
    
    return render(request, 'add_paciente.html', {'form': form})