from django.urls import path
from App1.views import IndexView, LoginView, RegisterView, cursos_view, crear_usuario, UserView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('user/', views.UserView, name='user'),
    path('logout/', views.LogoutView, name='logout'),
    path('agregar_favorito/<int:curso_id>/', views.agregar_favorito, name='agregar_favorito'),
    path('eliminar_favorito/<int:curso_id>/', views.eliminar_favorito, name='eliminar_favorito'),
    path('ver_favoritos/', views.ver_favoritos, name='ver_favoritos'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]