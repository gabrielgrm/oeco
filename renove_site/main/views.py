from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm


def index(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        password = request.POST['password']
        user = authenticate(request, username=cnpj, password=password)
        if user is not None:
            login(request, user)
            return redirect('renove_site\main\templates\main\home.html')  # Redirecionar para a página inicial
        else:
            messages.error(request, 'CNPJ ou senha incorretos.')
    return render(request, 'main/login.html')

@login_required
def home_view(request):
    return render(request, 'main/home.html')

@login_required
def view_appointments(request):
    # Aqui você pode recuperar os agendamentos do banco de dados
    return render(request, 'main/view_appointments.html')

@login_required
def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('view_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'main/new_appointment.html', {'form': form})

def comprovante(request):
    return render(request, 'comprovante.html')