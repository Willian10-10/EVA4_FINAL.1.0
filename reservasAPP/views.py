from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

# Vista para la página principal
from django.shortcuts import render
from .models import Reserva

from django.shortcuts import render

def index(request):
    return render(request, 'reservasAPP/index.html')



# Vista para listar todas las reservas
def reservas_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservasAPP/reservas_list.html', {'reservas': reservas})

# Vista para crear una nueva reserva
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Cambia 'index' al nombre de tu URL principal
    else:
        form = ReservaForm()

    return render(request, 'reservasAPP/crear_reserva.html', {'form': form})

# Vista para ver los detalles de una reserva
def detalle_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'detalle_reserva.html', {'reserva': reserva})

# Vista para editar una reserva existente
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas_list')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form})

# Vista para eliminar una reserva
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reservas_list')
