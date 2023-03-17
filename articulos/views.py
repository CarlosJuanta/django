from django.shortcuts import render, redirect
from .models import Articulos
from articulos.forms import ArticuloForm
import pandas as pd
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def listar_articulos(request):
    articulos =Articulos.objects.all()
    print(articulos)
    categoria = Articulos.objects.values('categoria').annotate(cantidad=Count('categoria')).order_by()
    nombres = pd.DataFrame(categoria)
    numeros = nombres.cantidad.tolist()
    nombres=nombres['categoria'].tolist()
    
    grafica ={'nombres': nombres,'numeros': numeros}
    return render(request, 'listar_articulos.html', {'articulos': articulos, 'grafica': grafica})

def crear_articulo(request):
    articulo = Articulos(codigo=request.POST['codigo'], descripcion=request.POST['descripcion'],
                         precio=request.POST['precio'], cantidad=request.POST['cantidad'],
                          categoria=request.POST['categoria'], descripcioncat=request.POST['descripcioncat'] )
    articulo.save()
    return redirect('/articulos')


def eliminar_articulo(request, articulo_id):
    articulo = Articulos.objects.get(id=articulo_id) 
    articulo.delete()
    return redirect('/articulos') 

def actualizar_articulo(request, articulo_id):
    articulo = Articulos.objects.get(id=articulo_id) 
   
    return render(request, 'editar_articulos.html', {'articulos': articulo})

def UpdateArticulo(request, articulo_id):
    updatearticulo = Articulos.objects.get(id= articulo_id)
    form = ArticuloForm(request.POST, instance=updatearticulo)
    if form.is_valid():
        form.save()
        messages.success(request, "Articulo actualizado correctamente")
        return render(request, 'editar_articulos.html', {"articulos":updatearticulo})
    

    

 





