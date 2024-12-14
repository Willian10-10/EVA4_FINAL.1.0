from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservas/', views.reservas_list, name='reservas_list'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/<int:id>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
]
