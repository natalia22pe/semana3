import requests
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AprendizForm
from .models import Aprendiz


def index(request):
  aprendices = Aprendiz.objects.all()
  return render(request, 'aprendices/index.html', {'aprendices': aprendices})


# 1. BUSCADOR DE APRENDICES
def buscar_aprendiz(request):
  query = request.GET.get('q', '')
  if query:
    aprendices = Aprendiz.objects.filter(nombre__icontains=query) | Aprendiz.objects.filter(
        documento__icontains=query
    )
  else:
    aprendices = Aprendiz.objects.none()
  return render(
      request, 'aprendices/index.html', {'aprendices': aprendices, 'query': query}
  )


# 2. CONSUMO DE API EXTERNA (Ej: Días Festivos o Datos Abiertos)
import requests
from django.shortcuts import render

def consumir_api(request):
    url = "https://date.nager.at/api/v3/PublicHolidays/2026/CO"
    festivos = []
    
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            festivos = response.json()
    except Exception as e:
        print(f"Error de conexión con la API externa: {e}")
        
    # Si la API falla o no hay internet, cargamos datos de respaldo locales para la clase
    if not festivos:
        festivos = [
            {"date": "2026-01-01", "localName": "Año Nuevo"},
            {"date": "2026-01-12", "localName": "Día de los Reyes Magos"},
            {"date": "2026-03-23", "localName": "Día de San José"},
            {"date": "2026-04-02", "localName": "Jueves Santo"},
            {"date": "2026-04-03", "localName": "Viernes Santo"},
            {"date": "2026-05-01", "localName": "Día del Trabajo"},
            {"date": "2026-05-18", "localName": "Día de la Ascensión"},
            {"date": "2026-06-08", "localName": "Corpus Christi"},
            {"date": "2026-06-15", "localName": "Sagrado Corazón"},
            {"date": "2026-06-29", "localName": "San Pedro y San Pablo"},
            {"date": "2026-07-20", "localName": "Día de la Independencia"},
            {"date": "2026-08-07", "localName": "Batalla de Boyacá"},
            {"date": "2026-08-17", "localName": "La Asunción de la Virgen"},
            {"date": "2026-10-12", "localName": "Día de la Raza"},
            {"date": "2026-11-02", "localName": "Todos los Santos"},
            {"date": "2026-11-16", "localName": "Independencia de Cartagena"},
            {"date": "2026-12-08", "localName": "Inmaculada Concepción"},
            {"date": "2026-12-25", "localName": "Navidad"}
        ]

    return render(request, 'aprendices/api_externa.html', {'festivos': festivos})

# 3. CRUD: CREAR, EDITAR, ELIMINAR
def crear_aprendiz(request):
  if request.method == 'POST':
    form = AprendizForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = AprendizForm()
  return render(request, 'aprendices/crear.html', {'form': form})


def editar_aprendiz(request, pk):
  aprendiz = get_object_or_404(Aprendiz, pk=pk)
  if request.method == 'POST':
    form = AprendizForm(request.POST, instance=aprendiz)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = AprendizForm(instance=aprendiz)
  return render(
      request, 'aprendices/editar.html', {'form': form, 'aprendiz': aprendiz}
  )


def eliminar_aprendiz(request, pk):
  aprendiz = get_object_or_404(Aprendiz, pk=pk)
  if request.method == 'POST':
    aprendiz.delete()
    return redirect('index')
  return render(request, 'aprendices/eliminar.html', {'aprendiz': aprendiz})


from rest_framework import viewsets
from .models import Aprendiz, Programa, Instructores, Competencias
from .serializers import AprendizSerializer, ProgramaSerializer

# Vistas de la API interna (Django REST Framework)
class AprendizViewSet(viewsets.ModelViewSet):
    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer