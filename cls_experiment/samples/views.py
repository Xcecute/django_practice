from django.shortcuts import render, redirect
from .models import Experiment, Sample
from .forms import ExperimentForm, SampleForm
from django.forms import inlineformset_factory

def experiment_list(request):
    experiments = Experiment.objects.all()
    return render(request, 'samples/experiment_list.html', {'experiments': experiments})

def add_experiment(request):
    ExperimentFormSet = inlineformset_factory(Experiment, Sample, form=SampleForm, extra=1)
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        formset = ExperimentFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            experiment = form.save()
            samples = formset.save(commit=False)
            for sample in samples:
                sample.experiment = experiment
                sample.save()
            return redirect('experiment_list')
    else:
        form = ExperimentForm()
        formset = ExperimentFormSet()
    return render(request, 'samples/add_experiment.html', {'form': form, 'formset': formset})
