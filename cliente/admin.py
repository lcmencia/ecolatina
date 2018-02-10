from __future__ import unicode_literals
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



class SectorInline(admin.StackedInline):
    model = Sector
    extra = 0

class AdminPropiedad(admin.ModelAdmin):
    inlines = [SectorInline]
    list_display = ('nombre', 'cliente', 'direccion')
    icon = '<i class="material-icons">business</i>'
    search_fields = ('nombre', 'cliente', 'direccion')
    raw_id_fields = ('cliente',)

class ControlInline(admin.StackedInline):
    model = Control
    extra = 0
    fieldsets = (
        (None, {'fields': ('estacion', 'operador', 'imagen', 'fecha', 'inicio', 'fin', 'observacion')}),
        ('Estado', {'fields': ('e_ausencia', 'e_buen_estado', 'e_consumido','e_deteriorado','e_capturado','e_pa_deteriorada','e_pa_buen_estado', 'e_no_acceso')}),
        ('Accion', {'fields': ('a_reposicion', 'a_limpieza', 'a_reemplazo')})
    )

class AdminEstacion(admin.ModelAdmin):
    inlines = [ControlInline]
    list_display = ('id','sector', 'fecha', )
    icon = '<i class="material-icons">bug_report</i>'
    raw_id_fields = ('sector',)
    



admin.site.register(Estacion, AdminEstacion)
admin.site.register(Sector, AdminSector)
admin.site.register(Cliente, AdminCliente)

admin.site.register(Propiedad, AdminPropiedad)



