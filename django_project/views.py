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

User = get_user_model()

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
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 22, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

