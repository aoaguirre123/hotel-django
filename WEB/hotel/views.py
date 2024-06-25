from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ServicioForm, PromocionForm
from .models import Servicio, Promocion
from django.conf import settings
from django.contrib.auth.decorators import login_required
import os 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm()
        })
        
    else:
        if request.POST['password1'] == request.POST['password1']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                        password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', { 
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error": 'Las contraseñas no coinciden'
                })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST
                ['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'El nombre o la contraseña es incorrecto'
            })
        else:
            login(request, user)
            return redirect('home')

@login_required
def crear_servicio(request):
    if request.method == 'GET':
        return render(request, 'crear_servicio.html', {
            'form': ServicioForm
        })
    else:
        try:
            form = ServicioForm(request.POST, request.FILES)
            new_servicio = form.save(commit=False)
            new_servicio.save()
            return redirect('servicio')
        except ValueError:
            return render(request, 'crear_servicio.html', {
            'form': ServicioForm,
            'error': 'Porfavor provee datos validos'
            })

@login_required        
def servicio(request):
    if not request.user.is_staff:
        return redirect('home')
    else:
        servicios = Servicio.objects.all()
        return render(request, 'servicio.html', {'servicios': servicios})

@login_required  
def detalle_servicio(request, servicio_id):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'GET':
        servicio = get_object_or_404(Servicio, pk=servicio_id)
        form = ServicioForm(instance=servicio)
        return render(request, 'detalle_servicio.html', {'servicio': servicio, 'form': form})
    else:
        servicio = get_object_or_404(Servicio, pk=servicio_id)
        form = ServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            imagen_nueva = form.cleaned_data.get('imagen')
            if imagen_nueva:
                # Verifica si la imagen ya existe en la carpeta media
                imagen_path = os.path.join(settings.MEDIA_ROOT, 'servicios', imagen_nueva.name)
                if os.path.exists(imagen_path):
                    # La imagen ya existe, Se asigna el path de la imagen existente
                    servicio.imagen = os.path.join('servicios', imagen_nueva.name)
                else:
                    # La imagen no existe, guardamos la nueva imagen con su respectivo path
                    servicio.imagen = imagen_nueva
            servicio.save()
            return redirect('servicio')
        else:
            return render(request, 'detalle_servicio.html', {'servicio': servicio, 'form': form, 'error': 'Error al actualizar el servicio'})
        
@login_required
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicio')

@login_required
def crear_promocion(request):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'crear_promocion.html', {
            'form': PromocionForm
        })
    else:
        try:
            form = PromocionForm(request.POST, request.FILES)
            new_promocion = form.save(commit=False)
            new_promocion.save()
            return redirect('promocion')
        except ValueError:
            return render(request, 'crear_promocion.html', {
            'form': PromocionForm,
            'error': 'Porfavor provee datos validos'
            })
        
@login_required
def promocion(request):
    if not request.user.is_staff:
        return redirect('home')
    else:
        promociones = Promocion.objects.all()
        return render(request, 'promocion.html', {'promociones': promociones})
        
@login_required
def detalle_promocion(request, promocion_id):
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'GET':
        promocion = get_object_or_404(Promocion, pk=promocion_id)
        form = PromocionForm(instance=promocion)
        return render(request, 'detalle_promocion.html', {'promocion': promocion, 'form': form})
    else:
        try:
            promocion = get_object_or_404(Promocion, pk=promocion_id)
            form = PromocionForm(request.POST, instance=promocion)
            form.save()
            return redirect('promocion')
        except ValueError:
            return render(request, 'detalle_promocion.html', {'promocion': promocion, 'form': form, 'error': "Error al actualizar la Promocion"})
        
@login_required
def eliminar_promocion(request, promocion_id):
    promocion = get_object_or_404(Promocion, pk=promocion_id)
    if request.method == 'POST':
        promocion.delete()
        return redirect('promocion')
    

def servicioCl(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicioCl.html', {'servicios': servicios})