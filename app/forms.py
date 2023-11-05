from django.forms import ModelForm
from .models import Programmer, JuniorProgrammer

class ProgrammerForm(ModelForm):
    class Meta:
        model = Programmer
        fields = ('__all__')
        
class JuniorProgrammerForm(ModelForm):
    class Meta:
        model = JuniorProgrammer
        fields = ('__all__')