from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def index(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.method == 'POST':
        cnpj = request.POST['cnpj']
        password = request.POST['password']
        user = authenticate(request, username=cnpj, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'CNPJ ou senha incorretos.')
    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})