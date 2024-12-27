from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_signup(request):
    if request.method == 'POST':
        if 'signup-form' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Error en el formulario de registro')
        elif 'login-form' in request.POST:
            email = request.POST['loginemail']
            password = request.POST['loginPassword']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Credenciales inválidas')
    else:
        form = SignUpForm()
    
    return render(request, 'authentication/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'authentication/profile.html')
