from django.urls import path
from . import views

urlpatterns = [
    path('citas/', views.citas_view, name='citas'),
    path('generar-turno/', views.generar_turno_view, name='generar_turno'),
    path('agendar-cita/', views.agendar_cita_view, name='agendar_cita'),
]
