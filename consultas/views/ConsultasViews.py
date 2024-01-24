from django.shortcuts import render, redirect, get_object_or_404
from .forms import PreOpForm, PosOpForm, ExamsForm, ConsultationForm, FormBaseForm
from .models import Exams, Consultation, FormBase

def add_consultation(request):
    pre_op_form = PreOpForm()
    pos_op_form = PosOpForm()
    exame_form = ExamsForm()
    form_base_form = FormBaseForm()

    if request.method == 'POST':
        consultation_form = ConsultationForm(request.POST)
        if consultation_form.is_valid():
            consultation = consultation_form.save()
            
            if 'include_exams' in request.POST:  
                exame_form = ExamsForm(request.POST)
                if exame_form.is_valid():
                    exame = exame_form.save(commit=False)
                    exame.consultation = consultation
                    exame.save()

            form_base = FormBase(consultation=consultation)
            form_base.save()

            pre_op_form = PreOpForm(request.POST)
            if pre_op_form.is_valid():
                pre_op = pre_op_form.save(commit=False)
                pre_op.consultation = consultation
                pre_op.save()

            pos_op_form = PosOpForm(request.POST)
            if pos_op_form.is_valid():
                pos_op = pos_op_form.save(commit=False)
                pos_op.consultation = consultation
                pos_op.save()
        else:
            pass
    else:
        consultation_form = ConsultationForm()

    context = {
        'add_consultation': consultation_form,
        'pre_op_form': pre_op_form,
        'pos_op_form': pos_op_form,
        'exame_form': exame_form,
        'form_base_form': form_base_form
    }

    return render(request, 'add_consultation.html', context)

def list_consultations(request):
    consultations = Consultation.objects.all()
    context = {
        'consultations': consultations
    }
    return render(request, 'list_consultations.html', context)

def edit_consultation(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    form_base_instance = get_object_or_404(FormBase, consultation=consultation)

    if request.method == 'POST':
        consultation_form = ConsultationForm(request.POST, instance=consultation)
        form_base_form = FormBaseForm(request.POST, instance=form_base_instance)
        if consultation_form.is_valid() and form_base_form.is_valid():
            consultation_form.save()
            form_base_form.save()
            return redirect('list_consultations')
    else:
        consultation_form = ConsultationForm(instance=consultation)
        form_base_form = FormBaseForm(instance=form_base_instance)

    context = {
        'consultation_form': consultation_form,
        'form_base_form': form_base_form
    }

    return render(request, 'edit_consultation.html', context)