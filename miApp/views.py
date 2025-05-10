from django.shortcuts import render,get_object_or_404
from .models import Principal, Categoria

def tu_vista_principal(request):
    categorias = Categoria.objects.all()  
    productos = Principal.objects.all()
    mas_vendidos=Principal.objects.order_by('Unidades_Vendidas')[:5]
    query = request.GET.get('q')  
    if query:
        productos = Principal.objects.filter(Nombre__icontains=query) 
    else:
        productos = Principal.objects.all()   
    return render(request, 'principal.html', {'producto': productos, 'categorias': categorias,'mas_vendidos':mas_vendidos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Principal, id=producto_id)
    return render(request, 'detalles.html', {'producto': producto})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    productos = Principal.objects.filter(categoria=categoria)
    
    return render(request, 'principal.html', {
        'producto': productos,
        'categorias': Categoria.objects.all(), 
        'categoria_actual': categoria 
    })