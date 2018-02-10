from __future__ import unicode_literals
from django.contrib import admin
from .models import *

# Register your models here.
class AdminFuncionario(admin.ModelAdmin):
    list_display = ('nombre', 'ruc', 'telefono', 'email', 'direccion')
    icon = '<i class="material-icons">work</i>'
    search_fields = ('nombre', 'ruc', 'direccion', 'telefono', 'email')

admin.site.register(Funcionario, AdminFuncionario)