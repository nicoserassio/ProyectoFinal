
from django.urls import path
from .views import *

urlpatterns = [
    path('acerca/', acercademi, name='acerca'),
    path('', PostList, name='index'),
    path('postdetail/<id>', postdetail, name='postdetail'),
    path('nuevopost/', crearpost, name="nuevopost"),
    path('eliminar/<id>', borrarpost, name='eliminar'),
    path('editpost/<id>', editpost, name='editpost'),

]
