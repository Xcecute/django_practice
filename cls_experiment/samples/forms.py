from django import forms
from .models import Experiment, Sample

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['project_code', 'visit_date']

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['name', 'quantity']
