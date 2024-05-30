from django.contrib import admin
from .models import Experiment, Sample

class SampleInline(admin.TabularInline):
    model = Sample

class ExperimentAdmin(admin.ModelAdmin):
    inlines = [SampleInline]

admin.site.register(Experiment, ExperimentAdmin)
