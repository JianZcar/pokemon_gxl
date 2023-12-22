from django.views.generic.list import ListView
from django.shortcuts import render
from cardquest.models import Trainer, PokemonCard, Collection
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from cardquest.forms import TrainerForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from cardquest.models import Trainer
# Create your views here.


def home_page_view(request):
    home = PokemonCard.objects.all()
    return render(request, 'home.html', {'home': home})


def trainers_view(request):
    trainer_list = Trainer.objects.all().order_by('id')
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


def trainer_edit_view(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainers')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_edit.html', {'form': form})


def trainer_delete_view(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        # delete trainer
        trainer.delete()
        return redirect('trainers')
    else:
        # confirm deletion
        return render(request, 'trainer_confirm_delete.html', {'trainer': trainer})

