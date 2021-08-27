from django.urls import path
from core.registro.views import RegistroCreateView


urlpatterns = [
    path('registro/', RegistroCreateView.as_view(), name='registro'),
]
