from django import forms

class GenerarTurnoForm(forms.Form):
    MOVIMIENTO_OPTIONS = [
        ("Movimiento", "Movimiento"),
        ("Entrega de chequeras", "Entrega de chequeras"),
        ("Apertura", "Apertura"),
        ("Consultas", "Consultas"),
        ("Mantenimiento de cuenta", "Mantenimiento de cuenta"),
    ]
    
    movimiento = forms.ChoiceField(
        choices=MOVIMIENTO_OPTIONS,
        label="Selecciona un movimiento",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class AgendarCitaForm(forms.Form):
    SUCURSAL_OPTIONS = [
        ("Sucursal uno", "Sucursal uno"),
        ("Sucursal dos", "Sucursal dos"),
        ("Sucursal tres", "Sucursal tres"),
    ]

    DIA_OPTIONS = [
        ("Lunes", "Lunes"),
        ("Martes", "Martes"),
        ("Miércoles", "Miércoles"),
        ("Jueves", "Jueves"),
        ("Viernes", "Viernes"),
        ("Sábado", "Sábado"),
        ("Domingo", "Domingo"),
    ]

    HORA_OPTIONS = [
        ("8:00 AM", "8:00 AM"),
        ("8:30 AM", "8:30 AM"),
        ("9:00 AM", "9:00 AM"),
        ("9:30 AM", "9:30 AM"),
        ("10:00 AM", "10:00 AM"),
        ("10:30 AM", "10:30 AM"),
        ("11:00 AM", "11:00 AM"),
        ("11:30 AM", "11:30 AM"),
        ("12:00 PM", "12:00 PM"),
    ]

    MOVIMIENTO_OPTIONS = [
        ("Cita apertura", "Cita apertura"),
        ("Fondo de inversión", "Fondo de inversión"),
        ("Créditos", "Créditos"),
        ("Entrega de tarjetas", "Entrega de tarjetas"),
        ("Actualizar datos", "Actualizar datos"),
        ("Banca digital", "Banca digital"),
    ]
    
    sucursal = forms.ChoiceField(
        choices=SUCURSAL_OPTIONS,
        label="Selecciona una sucursal",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    dia = forms.ChoiceField(
        choices=DIA_OPTIONS,
        label="Selecciona un día",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    hora = forms.ChoiceField(
        choices=HORA_OPTIONS,
        label="Selecciona una hora",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    movimiento = forms.ChoiceField(
        choices=MOVIMIENTO_OPTIONS,
        label="Selecciona un movimiento",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
