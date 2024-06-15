from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Curso, Usuarios, Favoritos
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def IndexView(request):
    """Página de inicio"""
    cursos = Curso.objects.all()  # Obtener todos los cursos siempre
    user = request.user if request.user.is_authenticated else None
    usuario = None

    if user:
        try:
            usuario = user.usuarios  # Intenta acceder al objeto Usuarios asociado al User
        except Usuarios.DoesNotExist:
            print("No existe un objeto Usuarios asociado a este usuario")

    context = {'cursos': cursos, 'user': user, 'usuario': usuario}
    return render(request, "index.html", context=context)

# def LoginView(request):
    """Página de login"""
    # return render(request, "login.html")

# Ejemplo de vista de login personalizada
def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('password')
        print(email, contraseña)
        user = authenticate(request, username=email, password=contraseña)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirige a la página principal después del login exitoso
        else:
            # Manejar caso de login fallido
            # Puedes mostrar un mensaje de error o redirigir de nuevo al login
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas.'})
    
    # Si el método no es POST, renderiza el formulario de login vacío
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
        
        # Crea un usuario en el modelo de usuario de Django
        user = User.objects.create_user(username=email, email=email, password=contraseña)
        
        # Hashea la contraseña antes de guardarla en el modelo Usuarios
        hashed_password = make_password(contraseña)
        
        # Crea una instancia de Usuarios asociada a este usuario
        usuario = Usuarios(user=user, nombre=nombre, apellido=apellido, email=email, contraseña=hashed_password, birthday=birthday)
        
        usuario.save()  # Guarda el usuario en la base de datos

        return redirect('/login')  # Redirige después de guardar el usuario
    
    # Si el método no es POST, renderiza el formulario vacío
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
            usuario = user.usuarios  # Intenta acceder al objeto Usuarios asociado al User
        except Usuarios.DoesNotExist:
            print("No existe un objeto Usuarios asociado a este usuario")

    context = {'user': user, 'usuario': usuario}
    return render(request, "user.html", context=context)

def LogoutView(request):
    logout(request)
    return redirect('/')

@login_required
def like_course(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    usuario = request.user.usuarios

    # Verificar si el curso ya está en favoritos
    if Favoritos.objects.filter(usuario=usuario, curso=curso).exists():
        # Si ya está en favoritos, eliminarlo
        Favoritos.objects.filter(usuario=usuario, curso=curso).delete()
    else:
        # Si no está en favoritos, agregarlo
        Favoritos.objects.create(usuario=usuario, curso=curso)

    return redirect('index')  # Redirigir a la página principal después de la acción

@login_required
def UserView(request):
    """Página de usuario"""
    user = request.user if request.user.is_authenticated else None
    usuario = None
    favoritos = []

    if user:
        try:
            usuario = user.usuarios  # Intenta acceder al objeto Usuarios asociado al User
            favoritos = usuario.favoritos.all()  # Obtén todos los cursos favoritos del usuario
        except Usuarios.DoesNotExist:
            print("No existe un objeto Usuarios asociado a este usuario")

    context = {'user': user, 'usuario': usuario, 'favoritos': favoritos}
    return render(request, "user.html", context=context)