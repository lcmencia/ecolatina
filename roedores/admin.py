from django.contrib import admin
from .models import Estacion, Control, Estado, Accion
# Register your models here.
class ControlInline(admin.StackedInline):
    model = Control
    extra = 0

class AdminEstacion(admin.ModelAdmin):
    inlines = [ControlInline]
    list_display = ('id','sector','propiedad', 'cliente', 'fecha', )
    icon = '<i class="material-icons">bug_report</i>'
    raw_id_fields = ('sector',)
    

class AdminEstado(admin.ModelAdmin):
    icon = '<i class="material-icons">warning</i>'

class AdminAccion(admin.ModelAdmin):
    icon = '<i class="material-icons">healing</i>'

admin.site.register(Estacion, AdminEstacion)
admin.site.register(Estado, AdminEstado)
admin.site.register(Accion, AdminAccion)