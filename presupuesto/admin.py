# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.

class AdminPresupuesto(admin.ModelAdmin):
    list_display = ('timestamp', 'email', 'empresa', 'nombre', 'telefono','respondido')
    readonly_fields=('timestamp', 'email', 'empresa', 'nombre', 'telefono','mensaje')


admin.site.register(Presupuesto, AdminPresupuesto)