from django.forms import ModelForm
from django import forms
from .models import Trainer, Collection, PokemonCard


class TrainerForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Trainer
        fields = '__all__'