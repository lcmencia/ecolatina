from django.db import models
from django.forms import ModelForm
from django import forms

class Presupuesto(models.Model):
    nombre = models.CharField(max_length=100,blank=True, null=True)
    telefono = models.CharField(max_length=100,blank=True, null=True)
    empresa = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField()
    mensaje = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class PresupuestoForm(ModelForm):
    
    class Meta:
        model = Presupuesto
        fields = [
            'nombre',
            'telefono',
            'empresa',
            'email',
            'mensaje',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'mensaje': forms.Textarea(attrs={'class':'form-control'}), 
         } 