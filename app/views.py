from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Programmer, JuniorProgrammer
from .forms import ProgrammerForm, JuniorProgrammerForm

class CreateProgrammer(CreateView):
    model = Programmer
    form_class = ProgrammerForm
    template_name = 'create_programmer.html'
    success_url = reverse_lazy('list')
    
class CreateJuniorProgrammer(CreateView):
    model = JuniorProgrammer
    form_class = JuniorProgrammerForm
    template_name = 'create_junior.html'
    success_url = reverse_lazy('list')
    
class List(ListView):
    model = Programmer
    template_name = 'list.html'
    context_object_name = 'programmers'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['juniors'] = JuniorProgrammer.objects.all()
        return context