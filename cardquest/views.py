from django.views.generic.list import ListView
from django.shortcuts import render
from cardquest.models import Trainer, PokemonCard, Collection
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from cardquest.forms import TrainerForm
from django.urls import reverse_lazy
# Create your views here.


def home_page_view(request):
    home = PokemonCard.objects.all()
    return render(request, 'home.html', {'home': home})


def trainers_view(request):
    trainer_list = Trainer.objects.all()
    paginator = Paginator(trainer_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    is_paginated = page_obj.has_other_pages()

    return render(request, 'trainers.html', {'page_obj': page_obj, 'is_paginated': is_paginated})


def trainers_create_view(request):
    form = TrainerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TrainerForm()

    context = {
        'form': form
    }
    return render(request, 'trainer_add.html', context)


def cards_view(request):
    cards = PokemonCard.objects.all()
    return render(request, 'cards.html', {'cards': cards})


def collections_view(request):
    collections = Collection.objects.all()
    return render(request, 'collections.html', {'collections': collections})

