from django.forms import ModelForm
from django import forms
from .models import Trainer, Collection, PokemonCard


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
