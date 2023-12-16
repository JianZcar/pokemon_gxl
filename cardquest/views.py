from django.views.generic.list import ListView
from django.shortcuts import render
from cardquest.models import Trainer, PokemonCard, Collection
# Create your views here.


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainers})


def cards(request):
    cards = PokemonCard.objects.all()
    return render(request, 'cards.html', {'cards': cards})


def collections(request):
    collections = Collection.objects.all()
    return render(request, 'collections.html', {'collections': collections})

