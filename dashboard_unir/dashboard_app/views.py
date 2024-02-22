from django.shortcuts import render
from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017')
mydatabase = client.dashboard

def home(request):
    return render(request, 'home.html')

def exit(request):
    return render(request, 'home.html')

def ver_coleccion(request):
    # Obtiene la lista de colecciones y las ordena alfabéticamente
    colecciones = sorted(mydatabase.list_collection_names())

    # Renderiza la página 'ver_coleccion' con la lista de colecciones
    return render(request, 'ver_coleccion.html', {'colecciones': colecciones})

def mostrar_coleccion(request):
    return render(request, 'detalle_coleccion.html')

def create_user(request):
    return render(request, 'crear_usuario.html')