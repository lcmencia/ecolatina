from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from usuario.models import *
from roedores.models import *
# Charts
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime, time
from dateutil.relativedelta import relativedelta
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

@ensure_csrf_cookie
def authentication(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            action = request.POST.get('action', None)
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {})

@login_required(None, 'login', '/login/')
def logout_view(request):
    #@csrf_protect
    #@ensure_csrf_cookie
    logout(request)
    return redirect("/")

@login_required(None,'login','/login/')
def index_view(request):
    propiedades = Propiedad.objects.filter(cliente__usuario=request.user.id)
    totalPropiedades = propiedades.count()
    cebos = Estacion.objects.filter(usuario=request.user.id)
    controles = Control.objects.select_related("estacion").filter(estacion__usuario=request.user.id)
    controles_recientes = controles[:3]
    capturados = controles.filter(e_capturado=True) 
    totalPropiedades = propiedades.count()
    totalCebos = cebos.count()
    totalCapturados = capturados.count()
    return render(request, 'index.html',{
    'propiedades':propiedades,
    'totalPropiedades':totalPropiedades,
    'totalCebos': totalCebos,
    'totalCapturados': totalCapturados,
    'controles_recientes': controles_recientes, 
    })

@login_required(None,'login','/login/')
def control_view(request):
    controles = Control.objects.select_related("estacion").filter(estacion__usuario=request.user.id)
    return render(request, 'control.html',{
    'controles':controles,
    })

@login_required(None,'login','/login/')
def property_view(request):
    propiedades = Propiedad.objects.select_related("cliente").filter(cliente__usuario=request.user.id)
    return render(request, 'propiedad.html',{
    'propiedades':propiedades,
    })



class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        z = datetime.datetime.now()
        z_mes = z.month
        label_z_mes = z.strftime("%B-%Y")
        cantidad_z_mes = Control.objects.filter(fecha__month=z_mes).count()
        
        y = z - relativedelta(months=1)
        y_mes = y.month 
        label_y_mes = y.strftime("%B-%Y")
        cantidad_y_mes = Control.objects.filter(fecha__month=y_mes).count()
        
        x = y - relativedelta(months=1)
        x_mes = x.month 
        label_x_mes = x.strftime("%B-%Y")
        cantidad_x_mes = Control.objects.filter(fecha__month=x_mes).count()
        
        w = x - relativedelta(months=1)
        w_mes = w.month 
        label_w_mes = w.strftime("%B-%Y")
        cantidad_w_mes = Control.objects.filter(fecha__month=w_mes).count()
        
        v = w - relativedelta(months=1)
        v_mes = v.month 
        label_v_mes = v.strftime("%B-%Y")
        cantidad_v_mes = Control.objects.filter(fecha__month=v_mes).count()

        u = v - relativedelta(months=1)
        u_mes = u.month 
        label_u_mes = u.strftime("%B-%Y")
        cantidad_u_mes = Control.objects.filter(fecha__month=u_mes).count()


        labels = [label_u_mes, label_v_mes, label_w_mes, label_x_mes, label_y_mes, label_z_mes]
        default_items = [cantidad_u_mes, cantidad_v_mes, cantidad_w_mes, cantidad_x_mes, cantidad_y_mes, cantidad_z_mes]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


