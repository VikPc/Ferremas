from django.urls import path
from . import views
from .views import agregar_al_carrito, inicio, lista_productos, ver_carrito, registrar_usuario, login_usuario

urlpatterns = [
    path('', inicio, name='inicio'),  # Página de inicio
    path('productos/', lista_productos, name='lista_productos'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('login_usuario/', login_usuario, name='login_usuario'),
    #path('logout/', views.logout_usuario, name='logout'),
    path('logout/', views.logout_usuario, name='logout'),

]
