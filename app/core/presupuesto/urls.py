from django.urls import path

from core.presupuesto.views import *

urlpatterns = [
    path('presupuesto/', PresupuestoListView.as_view(), name='presupuesto'),
]