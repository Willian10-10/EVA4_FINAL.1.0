from django import forms
from .models import Reserva  # Importa correctamente el modelo Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'fecha_reserva', 'hora_reserva', 'numero_personas', 'comentarios']
