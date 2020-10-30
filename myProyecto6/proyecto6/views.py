from django.shortcuts import render
from .models import SliderIndex,ImagenGaleria,MisionyVision, Insumos

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_2
from django.contrib.auth.decorators import login_required,permission_required


def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})

def formulario(request):
    if request.POST:
        nombre = request.POST.get('txtNombre')
        apellido = request.POST.get('txtApellido')
        email = request.POST.get('txtCorreo')
        usuario = request.POST.get('txtNombreUsuario')
        pass1 = request.POST.get('txtPass1')
        pass2 = request.POST.get('txtPass2')

        if pass1!=pass2:
            return render(request,'web/formulario.html',{'msg':'Contraseña No Coinside'})
        
        try:
            usu = User.objects.get(username=usuario)
            return render(request,'web/formulario.html',{'msg':'Usuario ya Existe'})
        except:
            
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.username = usuario
            usu.set_password(pass1)
            usu.save()

            us = authenticate(request, username=usuario, password=pass1)
            login_2(request,us)

        autos = SliderIndex.objects.all()
        return render(request,'web/index.html',{'autos':autos})

    return render(request,'web/formulario.html')


def galeria(request):
    ImgGaleria = ImagenGaleria.objects.all()
    return render(request,'web/galeria.html',{'ImgGaleria':ImgGaleria})

def servicios(request):
    return render(request,'web/servicios.html')

def vision(request):
    myv = MisionyVision.objects.all()
    return render(request,'web/vision.html',{'myv':myv})

@login_required(login_url= '/login/')
@permission_required('proyecto6.view_insumos',login_url='/login/')
@permission_required('proyecto6.change_insumos',login_url='/login/')
def modificar(request):
    msg = ''
    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg = 'Producto Modificado'
        except:
            msg = 'No se Modifico el Producto'
    
    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos,'msg':msg})
        
@login_required(login_url= '/login/')
@permission_required('proyecto6.view_insumos',login_url='/login/')
def busqueda_mod(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/mod_productos.html',{'insumo':insumo})
    except: 
        msg='No Ubico el Producto'
    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos,'msg':msg})

    
@permission_required('proyecto6.delete_insumos',login_url='/login/')    
@login_required(login_url= '/login/')  
def eliminar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='Elimino Insumo'
    except: 
        msg='No Elimino Insumo'
    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos,'msg':msg})

@permission_required('proyecto6.view_insumos',login_url='/login/')
@login_required(login_url= '/login/')
def lista_insumos(request):
    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos})

@login_required(login_url= '/login/')
@permission_required('proyecto6.add_insumos',login_url='/login/')
def registroProductos(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")
        insumos = Insumos(
            nombre = nombre,
            precio = precio,
            descripcion = descripcion,
            stock = stock
        )
        insumos.save()
        return render(request,'web/registroProductos.html',{'msg':'Insumo Registrado'})

    return render(request,'web/registroProductos.html')  

def cerrar_sesion(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})

def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombreUsuario")
        password = request.POST.get("txtPass")
        us = authenticate(request, username=usuario,password=password)
        if us is not None and us.is_active:
           login_2(request,us)
           autos = SliderIndex.objects.all()
           return render(request,'web/index.html',{'autos':autos})       
        else:
            return render(request,'web/login.html',{'msg':'Usuario No Existe'})       
    return render(request,'web/login.html') 
            


        
         