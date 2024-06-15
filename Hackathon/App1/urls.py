from django.urls import path
from .views import IndexView, LoginView, RegisterView, UserView, LogoutView, crear_usuario, like_course

urlpatterns = [
    path('', IndexView, name='index'),
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('user/', UserView, name='user'),
    path('logout/', LogoutView, name='logout'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('like/<int:curso_id>/', like_course, name='like_course'),
]
