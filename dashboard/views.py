from .firebase import db
import random
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import GenerarTurnoForm, AgendarCitaForm

def citas_view(request):
    # Obtener todas las citas desde Firestore
    citas_ref = db.collection("Citas")
    docs = citas_ref.stream()
    
    # Transformar los documentos en un diccionario
    citas = []
    for doc in docs:
        cita = doc.to_dict()
        citas.append(cita)

    # Pasar los datos al template
    return render(request, 'dashboard/citas.html', {'citas': citas})

def generar_turno_view(request):
    if request.method == 'POST':
        form = GenerarTurnoForm(request.POST)
        if form.is_valid():
            movimiento = form.cleaned_data['movimiento']
            
            # Generar valores por defecto
            numero = f"T-Sucursal {random.randint(1000, 9999)}"
            turno = f"T-{random.randint(100, 999)}"
            tipo = "turno"
            status = "En espera"
            fecha_hora_agendada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Guardar en Firestore
            doc_ref = db.collection("Citas").document(numero)
            cita = {
                "numero": numero,
                "sucursal": "Sucursal uno",
                "dia": None,
                "hora": None,
                "turno": turno,
                "tipo": tipo,
                "status": status,
                "fecha_hora_agendada": fecha_hora_agendada,
                "movimiento": movimiento,
            }
            doc_ref.set(cita)

            # Enviar todos los datos al template
            return render(request, 'dashboard/turno_exitoso.html', {
                'tipo': tipo,
                'turno': turno,
                'sucursal': "Sucursal uno",
                'dia': "N/A",
                'hora': "N/A",
                'movimiento': movimiento
            })
    else:
        form = GenerarTurnoForm()
    return render(request, 'dashboard/generar_turno.html', {'form': form})

def agendar_cita_view(request):
    if request.method == 'POST':
        form = AgendarCitaForm(request.POST)
        if form.is_valid():
            sucursal = form.cleaned_data['sucursal']
            dia = form.cleaned_data['dia']
            hora = form.cleaned_data['hora']
            movimiento = form.cleaned_data['movimiento']
            
            # Generar valores por defecto
            numero = f"C-Sucursal {random.randint(1000, 9999)}"
            turno = f"C-{random.randint(100, 999)}"
            tipo = "cita"
            status = "En espera"
            fecha_hora_agendada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Guardar en Firestore
            doc_ref = db.collection("Citas").document(numero)
            cita = {
                "numero": numero,
                "sucursal": sucursal,
                "dia": dia,
                "hora": hora,
                "turno": turno,
                "tipo": tipo,
                "status": status,
                "fecha_hora_agendada": fecha_hora_agendada,
                "movimiento": movimiento,
            }
            doc_ref.set(cita)

            # Enviar todos los datos al template
            return render(request, 'dashboard/turno_exitoso.html', {
                'tipo': tipo,
                'turno': turno,
                'sucursal': sucursal,
                'dia': dia,
                'hora': hora,
                'movimiento': movimiento
            })
    else:
        form = AgendarCitaForm()
    return render(request, 'dashboard/agendar_cita.html', {'form': form})
