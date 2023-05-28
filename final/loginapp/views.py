from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserEditForm, CustomAuthenticationForm

TEMPLATES = {  # Utilizamos una constante para mantener en un solo lugar los valores de los templates
    'login': 'loginapp/login.html',
    'register': 'loginapp/register.html',
    'profile': 'loginapp/profile.html',
}
# Create your views here.


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return render(request, TEMPLATES['login'], {'form': CustomAuthenticationForm()})
    form = CustomAuthenticationForm(request, data=request.POST)
    if not form.is_valid():
        return render(request, TEMPLATES['login'], {'form': form, 'errors': {'type': 'error', 'value': 'error up'}})
    # Obtenemos usuario y contraseña
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    # Autenticamos el usuario
    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, TEMPLATES['login'], {'form': form, 'errors': {'type': 'error', 'value': 'error up'}})
    # En este punto el login es correcto
    login(request, user)
    return redirect('index')


def register_request(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return render(request, TEMPLATES['register'], {'form': CustomUserCreationForm()})

    form = CustomUserCreationForm(request.POST)

    if not form.is_valid():
        errors = [{'type': k, 'value': v}
                  for k, v in form.error_messages.items()]
        context = {
            'form': form,
            'errors': errors,
        }
        return render(request, TEMPLATES['register'], context)
    form.save()
    return redirect('index')


def logout_request(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('index')


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    current_user = request.user
    if request.method != 'POST':
        initial_state = {
            'email': current_user.email,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            
        }
        return render(request, TEMPLATES['profile'], {'form': CustomUserEditForm(initial=initial_state)})

    form = CustomUserEditForm(request.POST)

    if not form.is_valid():
        return render(request, TEMPLATES['profile'], {'form': form, 'error': f'Error en el formulario'})

    new_user_data = form.cleaned_data
    current_user.first_name = new_user_data['first_name']
    current_user.last_name = new_user_data['last_name']
    current_user.description = new_user_data['description']
    current_user.webpage = new_user_data['webpage']
    current_user.email = new_user_data['email']

    current_user.save()

    if new_user_data['password1']:
        current_user.password1 = new_user_data['password1']
        current_user.password2 = new_user_data['password2']
        current_user.save()

    return render(request, TEMPLATES['profile'], {'form': form, 'success': f'Cambios guardados correctamente'})


