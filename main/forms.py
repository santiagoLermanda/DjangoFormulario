from django import forms 
from .models import Suscriptor
from django.utils.translation import ugettext_lazy as _

class SusForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields= ['nombre', 'email']
        labels={
        'nombre':_('Escribe tu nombre'),
        'email':_('Introduce tu correo')
        }
        widgets = {
            'nombre': forms.Textarea(attrs={'class':'rellenito'})
        }