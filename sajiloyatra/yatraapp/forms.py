from django import forms

from yatraapp.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['location', 'event_name', 'description', 'month', 'date_created']
        widgets = {
              'location': forms.TextInput(attrs={'class': 'form-control','required' : 'required'}),
              'event_name': forms.TextInput(attrs={'class': 'form-control','required' : 'required'}),
              'description': forms.TextInput(attrs={'class': 'form-control','required' : 'required'}),
              'month': forms.TextInput(attrs={'class': 'form-control','required' : 'required'}),
              'date_created': forms.TextInput(attrs={'class': 'form-control','required' : 'required'}),
    }