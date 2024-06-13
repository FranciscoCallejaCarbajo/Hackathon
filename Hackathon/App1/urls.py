from django.urls import path
from App1.views import IndexView, LoginView, RegisterView

urlpatterns = [
    path('', IndexView),
    path('login' , LoginView),
    path('register' , RegisterView)
]