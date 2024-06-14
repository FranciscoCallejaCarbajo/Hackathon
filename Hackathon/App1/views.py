from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Usuarios, Favorito
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def IndexView(request):
    """Página de inicio"""
    cursos = Curso.objects.all() if request.user.is_authenticated else []
    user = request.user if request.user.is_authenticated else None
    usuario = None

    if user:
        try:
            usuario = user.usuarios  # Intenta acceder al objeto Usuarios asociado al User
        except Usuarios.DoesNotExist:
            print("No existe un objeto Usuarios asociado a este usuario")

    context = {'cursos': cursos, 'user': user, 'usuario': usuario}
    return render(request, "index.html", context=context)

def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('password')
        user = authenticate(request, username=email, password=contraseña)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirige a la página principal después del login exitoso
        else:
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas.'})
    
    return render(request, 'login.html')

def RegisterView(request):
    """Página de register"""
    return render(request, "register.html")

def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
        birthday = request.POST.get('birthday')
        
        user = User.objects.create_user(username=email, email=email, password=contraseña)
        usuario = Usuarios(user=user, nombre=nombre, apellido=apellido, email=email, contraseña=contraseña,
                        birthday=birthday)
        
        usuario.save()

        return redirect('/login')
    
    return render(request, 'crear_usuario.html')

@login_required
def cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def UserView(request):
    """Página de user"""
    user = request.user if request.user.is_authenticated else None
    usuario = None

    if user:
        try:
            usuario = user.usuarios
        except Usuarios.DoesNotExist:
            print("No existe un objeto Usuarios asociado a este usuario")

    context = {'user': user, 'usuario': usuario}
    return render(request, "user.html", context=context)

def LogoutView(request):
    logout(request)
    return redirect('/')

@login_required
def agregar_favorito(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    Favorito.objects.get_or_create(usuario=request.user.usuarios, curso=curso)
    return redirect('cursos')

@login_required
def eliminar_favorito(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    favorito = Favorito.objects.filter(usuario=request.user.usuarios, curso=curso)
    favorito.delete()
    return redirect('cursos')

@login_required
def ver_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user.usuarios)
    return render(request, 'favoritos.html', {'favoritos': favoritos})

@login_required
def perfil_usuario(request):
    usuario = request.user.usuarios
    favoritos = Favorito.objects.filter(usuario=usuario).select_related('curso')
    return render(request, 'perfil.html', {'usuario': usuario, 'favoritos': favoritos})
