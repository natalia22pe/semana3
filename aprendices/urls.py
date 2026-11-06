from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

# Creamos el router para la API interna instalada
router = DefaultRouter()
router.register(r'api/aprendices', views.AprendizViewSet)
router.register(r'api/programas', views.ProgramaViewSet)

urlpatterns = [
    # Rutas normales de tu CRUD y vistas web
    path('', views.index, name='index'),
    path('buscar/', views.buscar_aprendiz, name='buscar_aprendiz'),
    path('crear/', views.crear_aprendiz, name='crear_aprendiz'),
    path('editar/<int:pk>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('eliminar/<int:pk>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
    
    # Rutas de la API interna instalada (incluye todas las del router)
    path('', include(router.urls)),
]