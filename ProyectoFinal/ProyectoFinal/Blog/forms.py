from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'contenido')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


