#vista
from django.views.generic import ListView
#vista con detalle
from django.views.generic.detail import DetailView
#crear
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

