from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libros
from .forms import LibrosForm,UsuarioForm
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    libros = Libros.objects.all() 
    return render(request,'libros/index.html',{'libros':libros})

def crear_libro(request):
    formulario = LibrosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')   
    return render(request,'libros/crear.html', {'formulario':formulario})

def editar_libro(request,id_libro):
    libro = Libros.objects.get(id_libro=id_libro)
    formulario = LibrosForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html', {'formulario':formulario})

def eliminar_libro(request, id_libro):
    libro = Libros.objects.get(id_libro=id_libro)
    libro.delete()
    return redirect('libros')
