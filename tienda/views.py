from django.shortcuts import render
#
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.

from django.shortcuts import render, redirect
from .models import Producto

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse


# Mostrar productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})

# Mostrar carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())
    total = sum(producto.precio * carrito[str(producto.id)] for producto in productos)
    return render(request, 'tienda/carrito.html', {'productos': productos, 'carrito': carrito, 'total': total})

# Agregar al carrito
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id = str(producto_id)
    carrito[producto_id] = carrito.get(producto_id, 0) + 1
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def inicio(request):
    return render(request, 'tienda/inicio.html')

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
    return redirect('inicio')
# Agregar usaario
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseNotAllowed

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'username': user.username})
        else:
            return JsonResponse({'success': False, 'error': 'Credenciales incorrectas'})

    # Si no es método POST, devolver error 405 explícitamente
    return HttpResponseNotAllowed(['POST'])





def logout_usuario(request):
    logout(request)
    return redirect('inicio')
   
