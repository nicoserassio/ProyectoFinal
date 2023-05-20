from django.urls import path
from Blog import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.main),
    path('acerca', views.acercademi),
    path('login', views.login_request, name='Login' ),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='Blog/logout.html'), name='Logout'),
    path('curso/list', views.PostList, name='List'),
    path(r'^(?P<pk>\d+)$', views.PostDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.PostCrear.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.PostUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.PostDelete.as_view(),name='Delete')
    ]