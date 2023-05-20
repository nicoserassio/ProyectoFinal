from django.shortcuts import render
from Blog.models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#Vista Principal
def main(request):
    return render(request, 'Blog/main.html')
#Mostrar Acerca de Mi
def acercademi(request):
    return render(request, 'Blog/acerca.html')
@login_required
class PostList(ListView):
    model = Post
    template_name = 'Blog/verpost.html'
class PostDetalle(DetailView):
    model = Post
    template_name = 'Blog/postdetalle.html'
class PostUpdate(UpdateView):
    model = Post
    success_url = 'Blog/post/list'
    fields = ['titulo', 'subtitulo', 'contenido']
class PostCrear(CreateView):
    model = Post
    success_url = 'Blog/post/list'
    fields = ['titulo', 'subtitulo', 'contenido']
class PostDelete(DeleteView):
    model = PostCrear
    success_url = 'Blog/post/list'

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "Blog/main.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "Blog/login.html", {"mensaje":"Datos incorrectos"})           
        else:
            return render(request, "Blog/login.html", {"mensaje":"Usuario o contraseña incorrecta"})
    form = AuthenticationForm()
    return render(request, "Blog/login.html", {"form": form})

def register(request):
    form=UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'Blog/main.html', {'mensaje': 'Usuario Creado'})
    else:
        form=UserCreationForm()
    return render(request, 'Blog/register.html', {'form':form})    