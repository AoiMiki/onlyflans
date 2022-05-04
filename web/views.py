from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactFormForm
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'public_flans': public_flans})

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'private_flans': private_flans})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()
            
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password1']
            new_user = authenticate(username = usuario, password = contrasena)
            login(request, user = new_user)
            messages.success(request, f'Usuario {usuario} regístrado exitosamente')
            return HttpResponseRedirect('/bienvenido')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def buscaflanes(request):
    if request.method == 'POST':
        buscador = request.POST['buscador']

        flanes = Flan.objects.filter(name__contains = buscador)
        return render(request, 'results_flan.html', {
            'buscador': buscador,
            'flanes': flanes,
        })
    else:
        return render(request, 'results_flan.html', {})