from django.contrib import admin
from .models import *


class AdminSector(admin.ModelAdmin):
    list_display = ('propiedad', 'nombre')
    icon = '<i class="material-icons">work</i>'
    
    
class EncargadoInline(admin.StackedInline):
    model = Encargado
    extra = 0

class AdminCliente(admin.ModelAdmin):
    inlines = [EncargadoInline]
    list_display = ('razon_social', 'ruc', 'telefono', 'email',)
    icon = '<i class="material-icons">work</i>'
    search_fields = ('nombre', 'ruc','telefono', 'email')

class AdminFuncionario(admin.ModelAdmin):
    list_display = ('nombre', 'ruc', 'telefono', 'email', 'direccion')
    icon = '<i class="material-icons">work</i>'
    search_fields = ('nombre', 'ruc', 'direccion', 'telefono', 'email')

class SectorInline(admin.StackedInline):
    model = Sector
    extra = 0

class AdminPropiedad(admin.ModelAdmin):
    inlines = [SectorInline]
    list_display = ('nombre', 'cliente', 'direccion')
    icon = '<i class="material-icons">business</i>'
    search_fields = ('nombre', 'cliente', 'direccion')
    raw_id_fields = ('cliente',)


admin.site.register(Sector, AdminSector)
admin.site.register(Cliente, AdminCliente)
admin.site.register(Funcionario, AdminFuncionario)
admin.site.register(Propiedad, AdminPropiedad)



