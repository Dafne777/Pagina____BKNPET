from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, Producto
from .forms import ProductoForm, CustomUserCreationForm, MascotaForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from rest_framework import generics
from .serializers import ProductoSerializer, MascotaSerializer

from django.contrib.auth.decorators import login_required, permission_required

# ----------------------------------------------------------------------------------------------------
#                                   APP
def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def acerca_de(request):
    return render(request, 'app/acerca_de.html')

def registrar(request):
    return render(request, 'app/registrar.html')

def pokebusca(request):
    return render(request, 'app/pokebusca.html')


# ---------------------------------------------------------------------------------------------
#                   PRODUCTOS AGREGADOS RECIENTEMENTE
def recientes(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/recientes.html',data)


# ----------------------------------------------------------------------------------------------------
#                                           CRUD

@permission_required('app.add_producto')
def agregar_producto(request):
    
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El producto ha sido guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'CRUD/agregar.html', data)



def listar_productos(request):
    productos = Producto.objects.all()
    
    data = {
        'productos' : productos
    }
    return render(request, 'CRUD/listar.html', data)


@permission_required('app.change_producto')
def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar_producto")    
        data["form"] = formulario
    
    return render(request, 'CRUD/modificar.html',data)


@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar_producto")


# -----------------------------------------------------------------------------------------
#                           REGISTRO FUNCIONAL
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"],)
            login(request, user)
            # messages.success(request," Te has registrado correctamente")
            #redirigir al home
            return redirect(to="home")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html',data)

# -----------------------------------------------------------------------------------------------------
#                                           API LOCAL   

class API_objects(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


@api_view(['GET', 'POST'])
def producto_collection(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'  ])
def producto_element(request, pk):
    productos = get_object_or_404(Producto, id=pk)
    if request.method == 'GET':
        serializer = ProductoSerializer(productos)
        return Response(serializer.data)
    elif request.method =='PUT': 
        serializer = ProductoSerializer(productos, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = ProductoSerializer(productos, data= request.data)
        if serializer.is_valid():
            productos.delete()
            return Response (status=status.HTTP_204_NO_CONTENT)


#--------------------------------- API MASCOTAS -----------------------------------------------------
#
class API_objects(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


@api_view(['GET', 'POST'])
def mascota_collection(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MascotaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'  ])
def mascota_element(request, pk):
    mascotas = get_object_or_404(Mascota, id=pk)
    if request.method == 'GET':
        serializer = MascotaSerializer(mascotas)
        return Response(serializer.data)
    elif request.method =='PUT': 
        serializer = MascotaSerializer(mascotas, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MascotaSerializer(mascotas, data= request.data)
        if serializer.is_valid():
            mascotas.delete()
            return Response (status=status.HTTP_204_NO_CONTENT)




# ----------------------------------------------------------------------------------------------------
#                                           APP NUEVA   
def adopcion(request):
    mascotas = Mascota.objects.all()
    data = {
        'mascotas' : mascotas
    }
    return render(request, 'ADOP/adopcion.html', data)

@permission_required('app.add_mascota')
def agregar_mascota(request):
    data = {
        'form' : MascotaForm()
    }
    
    if request.method == 'POST':
        formulario = MascotaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "La mascota a sido agregada correctamente"
        else:
            data["form"] = formulario
    return render(request, 'ADOP/agregar_pet.html', data)


def listar_mascota(request):
    mascotas = Mascota.objects.all()
    
    data = {
        'mascotas' : mascotas
    }
    return render(request, 'ADOP/listar_pet.html', data)


def modificar_mascota(request, id):
    
    mascota = get_object_or_404(Mascota, id=id)
    
    data = {
        'form' : MascotaForm(instance=mascota)
    }
    
    if request.method =='POST':
        formulario = MascotaForm(data=request.POST, instance=mascota, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="listar_mascota")    
        data["form"] = formulario
    
    return render(request, 'ADOP/modificar_pet.html',data)


def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="listar_mascota")



# ----------------------------------------------------------------------------------------------------
#                                       PRODUCTOS

def producto1(request):
    return render(request, 'productos/producto1.html')

def producto2(request):
    return render(request, 'productos/producto2.html')

def producto3(request):
    return render(request, 'productos/producto3.html')

def producto4(request):
    return render(request, 'productos/producto4.html')

def producto5(request):
    return render(request, 'productos/producto5.html')

def producto6(request):
    return render(request, 'productos/producto6.html')

def producto7(request):
    return render(request, 'productos/producto7.html')

def producto8(request):
    return render(request, 'productos/producto8.html')





