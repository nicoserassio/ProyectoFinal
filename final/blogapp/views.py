from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
#vista de post
@login_required
def PostList(request):
    posteos = Post.objects.all()
    return render(request, 'blogapp/index.html', {'posteos':posteos})
#detalle del post
@login_required
def postdetail(request, id):
    posteo = Post.objects.get(id=id)
    return render(request, 'blogapp/postdetail.html', {'posteo': posteo})
#acerca de mi
def acercademi(request):
    return render(request, 'blogapp/acerca.html')
#crear post
@login_required
def crearpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            titulo = datos['titulo']
            resumen = datos['resumen']
            texto = datos['texto']
            autor = datos['autor']
            post = Post(titulo=titulo, resumen=resumen, texto=texto, autor=autor)
            post.save()
            return redirect('index')
        else:
            return render(request, "blogapp/index.html", {"form":form})       
    else: 
        form = PostForm()   
        return render(request, "blogapp/nuevopost.html", {"form":form})
#eliminar post
@login_required
def borrarpost(request, id):
    posteo = Post.objects.get(id=id)
    posteo.delete()
    return redirect('index')

def editpost(request, id):
    posteo = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            posteo.titulo = info["titulo"]
            posteo.resumen = info['resumen']
            posteo.texto = info['texto']
            posteo.autor = info['autor']
            posteo.save()
            return redirect('index') 
        else:
            return render(request, 'blogapp/index.html', {'form':form}) 
    else:
        form=PostForm(initial={'titulo':posteo.titulo, 'resumen':posteo.resumen, 'texto':posteo.texto, 'autor':posteo.autor})
        return render(request, 'blogapp/editpost.html', {'form':form, 'posteo':posteo})