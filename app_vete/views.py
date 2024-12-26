from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import PerfilUsuarioForm
from .models import Perfil


from.forms import MascotasFormulario, ClienteFormulario, ProductoFormulario, SucursalFormulario, EditarPerfilForm

from .models import (Sucursal, Producto, Cliente, Mascota)

# Create your views here.

def inicio_sesion(request):
    if request.method == "POST":
        password = request.POST.get("password")
        username = request.POST.get("username")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Sesion iniciada con éxito. Bienvenido {request.user.username}")
            return redirect("inicio")
        else:
            messages.error(request, f"No se pudo iniciar sesion. Por favor intente nuevamente")
            return redirect("inicio")


    else:
        return render(request, "app_vete/forms/inicio-sesion.html")

@login_required
def cerrar_sesion(request):
    logout(request)
    messages.warning(request, "Sesion cerrada con éxito. Hasta luego!")
    return redirect("inicio")


def registro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro-exitoso-usuario")
    

    else:
        form = UserCreationForm()
    return render(request, "app_vete/forms/registro-usuario.html", {"form": form})

@login_required
def mostrar_perfil(request):
    return render(request, "app_vete/forms/mostrar-perfil.html")

@login_required
def editar_perfil(request):

    usuario = request.user

    perfil, _ = Perfil.objects.get_or_create(user=usuario)

    if request.method == "POST":

        user_form = EditarPerfilForm(request.POST, instance=usuario)
        perfil_form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)


        if user_form.is_valid() and perfil_form.is_valid(): 
            user_form.save()
            perfil_form.save()
            messages.success(request, "Perfil actualizado con éxito.")
            return redirect("mostrar-perfil")
        else:
            messages.success(request, "No se pudieron actualizar tus datos.")
            return redirect("inicio")

    else:
        user_form = EditarPerfilForm(instance=usuario)
        perfil_form = PerfilUsuarioForm(instance=perfil)

    return render(request, "app_vete/forms/editar-perfil.html", {"user_form": user_form, "perfil_form": perfil_form})

@login_required
def cambiar_contraseña(request):

    usuario = request.user

    if request.method == "POST":
        contraseña_form = PasswordChangeForm(usuario, request.POST)
        if contraseña_form.is_valid():
            contraseña_form.save()
            update_session_auth_hash(request, usuario)
            messages.success(request, "Contraseña actualizada con éxito.")
            return redirect("inicio")
        else:
            return redirect("inicio")

    else:
        contraseña_form = PasswordChangeForm(usuario)

    return render(request, "app_vete/forms/cambiar-contraseña.html", {"contraseña_form": contraseña_form})



def inicio(request):
    return render(request,"app_vete/index.html")

def acerca(request):
    return render(request,"app_vete/acerca.html")

def sucursal(request):

    query = request.GET.get('q')

    if query:
        sucursales = Sucursal.objects.filter(Q(nombre__icontains=query) | Q(direccion__icontains=query) | Q(telefono__icontains=query))

    else:
        sucursales = Sucursal.objects.all()


    return render(request,"app_vete/sucursal.html", {"sucursales": sucursales})


def producto(request):

    query = request.GET.get('q')

    if query:
        producto = Producto.objects.filter(Q(nombre__icontains=query) | Q(precio__icontains=query) | Q(categoria__icontains=query))

    else:

        producto = Producto.objects.all()

    return render(request,"app_vete/producto.html", {"producto": producto})
    
@login_required
def cliente(request):

    query = request.GET.get('q')

    if query:
        cliente = Cliente.objects.filter(Q(nombre__icontains=query) | Q(telefono__icontains=query) | Q(email__icontains=query))


    else:
    
        cliente = Cliente.objects.all()
    print(cliente)
    return render(request,"app_vete/cliente.html", {"cliente": cliente})

@login_required
def mascota(request):

    query = request.GET.get('q')

    if query:
        mascota = Mascota.objects.filter(Q(especie__icontains=query) | Q(edad__icontains=query) | Q(raza__icontains=query)) | Q(nombre__icontains=query)
        
    else:

        mascota = Mascota.objects.all()

    return render(request,"app_vete/mascota.html", {"mascota": mascota})

@login_required
def formulario_mascota(request):

    if request.method == "POST":
        mascota_form = MascotasFormulario(request.POST)
        if mascota_form.is_valid():
            info_limpia = mascota_form.cleaned_data
            mascota = Mascota(nombre = info_limpia["nombre"], especie = info_limpia["especie"], raza = info_limpia["raza"], edad = info_limpia["edad"]) 
            mascota.save()
            return redirect("registro-exitoso")
        
    else:
        mascota_form = MascotasFormulario()
    contexto = {"mascota_form": mascota_form}
    print(contexto)
    return render(request, "app_vete/forms/mascota-formulario.html", contexto)

@login_required
def formulario_cliente(request):
    if request.method == "POST":
        cliente_form = ClienteFormulario(request.POST)
        if cliente_form.is_valid():
            info_limpia = cliente_form.cleaned_data
            cliente = Cliente(nombre=info_limpia["nombre"], telefono=info_limpia["telefono"], email=info_limpia["email"])
            cliente.save()
            return redirect("registro-exitoso")

    else:
        cliente_form = ClienteFormulario()
    contexto = {"cliente_form": cliente_form}
    return render(request, "app_vete/forms/cliente-formulario.html", contexto)

@login_required
def formulario_producto(request):
    if request.method == "POST":
        producto_form = ProductoFormulario(request.POST)
        if producto_form.is_valid():
            info_limpia = producto_form.cleaned_data
            producto = Producto(nombre=info_limpia["nombre"], precio=info_limpia["precio"], categoria=info_limpia["categoria"])
            producto.save()
            return redirect("registro-exitoso")
    else:
        producto_form = ProductoFormulario()
    contexto = {"producto_form": producto_form}
    return render(request, "app_vete/forms/producto-formulario.html", contexto)

@login_required
def formulario_sucursal(request):
    if request.method == "POST":
        sucursal_form = SucursalFormulario(request.POST)
        if sucursal_form.is_valid():
            info_limpia = sucursal_form.cleaned_data
            sucursal = Sucursal(nombre=info_limpia["nombre"], direccion=info_limpia["direccion"], telefono=info_limpia["telefono"])
            sucursal.save()
            return redirect("registro-exitoso")
    else:
        sucursal_form = SucursalFormulario()
    contexto = {"sucursal_form": sucursal_form}
    return render(request, "app_vete/forms/sucursal-formulario.html", contexto)

def registro_exitoso(request):
    return render(request,"app_vete/forms/registro-exitoso.html")

def registro_exitoso_usuario(request):
    return render(request,"app_vete/forms/registro-exitoso-usuario.html")

@login_required
def eliminar_producto(request, id):

    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.warning(request, "Producto eliminado.")
    return redirect("producto")

@login_required
def eliminar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    messages.warning(request, "Mascota eliminada.")
    return redirect("mascota")

@login_required
def eliminar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    messages.warning(request, "Cliente eliminado.")
    return redirect("cliente")

@login_required
def eliminar_sucursal(request, id):

    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    messages.warning(request, "Sucursal eliminada.")
    return redirect("sucursal")

@login_required
def editar_sucursal(request, id):

    sucursal = Sucursal.objects.get(id=id)

    if request.method == "POST":
        sucursal_form = SucursalFormulario(request.POST)
        if sucursal_form.is_valid():
            info_limpia = sucursal_form.cleaned_data
            sucursal.nombre = info_limpia["nombre"]
            sucursal.direccion = info_limpia["direccion"]
            sucursal.telefono = info_limpia["telefono"]
            sucursal.save()
            messages.success(request, "Sucursal editada con éxito.")
        return redirect("sucursal")

    else:
        sucursal = Sucursal.objects.get(id=id)
        sucursal_form = SucursalFormulario(initial={"nombre": sucursal.nombre, "direccion": sucursal.direccion , "telefono": sucursal.telefono})

    return render(request, "app_vete/forms/editar-sucursal.html", {"sucursal_form": sucursal_form})

@user_passes_test(lambda u: u.is_superuser)
def editar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)

    if request.method == "POST":
        mascota_form = MascotasFormulario(request.POST)
        if mascota_form.is_valid():
            info_limpia = mascota_form.cleaned_data
            mascota.nombre = info_limpia["nombre"]
            mascota.especie = info_limpia["especie"]
            mascota.raza = info_limpia["raza"]
            mascota.edad = info_limpia["edad"]
            mascota.save()
            messages.success(request, "Mascota editada con éxito.")
        return redirect("mascota")

    else:
        mascota = Mascota.objects.get(id=id)
        mascota_form = MascotasFormulario(initial={"nombre": mascota.nombre, "especie": mascota.especie, "raza": mascota.raza , "edad": mascota.edad})

    return render(request, "app_vete/forms/editar-mascota.html", {"mascota_form": mascota_form})

@login_required
def editar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)

    if request.method == "POST":
        cliente_form = ClienteFormulario(request.POST)
        if cliente_form.is_valid():
            info_limpia = cliente_form.cleaned_data
            cliente.nombre = info_limpia["nombre"]
            cliente.telefono = info_limpia["telefono"]
            cliente.email = info_limpia["email"]
            cliente.save()
            messages.success(request, "Cliente editada con éxito.")
        return redirect("cliente")

    else:
        cliente = Cliente.objects.get(id=id)
        cliente_form = ClienteFormulario(initial={"nombre": cliente.nombre, "telefono": cliente.telefono , "email": cliente.email})

    return render(request, "app_vete/forms/editar-cliente.html", {"cliente_form": cliente_form})

@login_required
def editar_producto(request, id):

    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        producto_form = ProductoFormulario(request.POST)
        if producto_form.is_valid():
            info_limpia = producto_form.cleaned_data
            producto.nombre = info_limpia["nombre"]
            producto.precio = info_limpia["precio"]
            producto.categoria = info_limpia["categoria"]
            producto.descripcion = info_limpia["descripcion"]
            producto.save()
            messages.success(request, "Producto editado con éxito.")
        return redirect("producto")

    else:
        producto = Producto.objects.get(id=id)
        producto_form = ProductoFormulario(initial={"nombre": producto.nombre, "precio": producto.precio , "categoria": producto.categoria, "descripcion": producto.descripcion})

    return render(request, "app_vete/forms/editar-producto.html", {"producto_form": producto_form})


def descripcion_producto(request, id):

    producto = Producto.objects.get(id=id)

    return render(request, 'app_vete/forms/descripcion-producto.html', {'producto': producto})

def pagina_remodelacion(request):
    return render(request,"app_vete/pagina-remodelacion.html")