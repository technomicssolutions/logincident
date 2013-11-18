from django.contrib import admin
from django.db import models
from django.views.generic.list import ListView
from .models import *

class WitnessInline(admin.TabularInline):
    model = Witness
    initial_forms = 3
    extra = 0

    fk_name = 'majorincident'
    list_display = ('name', 'address', 'credentials', 'date_of_birth')

class MajorIncidentAdmin(admin.ModelAdmin):
    inlines = [WitnessInline]
    list_display = ('injured_person_name', 'injured_person_role', 'severity','medical_attention')
    
admin.site.register(IncidentDetails)
admin.site.register(MinorIncident)
admin.site.register(Witness)
admin.site.register(MajorIncident, MajorIncidentAdmin)