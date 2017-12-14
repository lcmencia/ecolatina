from django.contrib import admin
from .models import Estacion, Control
# Register your models here.
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
    list_display = ('id','sector','propiedad', 'cliente', 'fecha', )
    icon = '<i class="material-icons">bug_report</i>'
    raw_id_fields = ('sector',)
    



admin.site.register(Estacion, AdminEstacion)
