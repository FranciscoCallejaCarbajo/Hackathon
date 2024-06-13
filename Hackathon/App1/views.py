from django.shortcuts import render

# Create your views here.
def IndexView(request):
    """Página de inicio"""
    return render(request, "index.html")

def LoginView(request):
    """Página de login"""
    return render(request, "login.html")

def RegisterView(request):
    """Página de register"""
    return render(request, "register.html")