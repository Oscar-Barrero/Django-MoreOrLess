from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.metas.forms import MetasForm
from core.metas.models import Metas


# Create your views here.
class MetasListView(ListView):
    model = Metas
    template_name = 'metas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MetasCreateView(CreateView):
    model = Metas
    form_class = MetasForm
    template_name = 'form_metas.html'
    success_url = reverse_lazy('metas')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ingresar meta'
        context['list_url'] = reverse_lazy('metas')
        context['action'] = 'add'
        return context


class MetasUpdateView(UpdateView):
    model = Metas
    form_class = MetasForm
    template_name = 'form_metas.html'
    success_url = reverse_lazy('metas')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar categoria'
        context['list_url'] = reverse_lazy('metas')
        context['action'] = 'edit'

        return context

class MetasDeleteView(DeleteView):
    model = Metas
    template_name = 'delete_metas.html'
    success_url = reverse_lazy('metas')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar meta'
        context['list_url'] = reverse_lazy('metas')
        return context