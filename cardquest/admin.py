from django.contrib import admin
from .models import Trainer, PokemonCard, Collection


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email', 'trainer_id')
    search_fields = ('name', 'location', 'email', 'trainer_id')


@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number',
                    'release_date', 'evolution_stage', 'abilities')
    search_fields = ('name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number',
                     'release_date', 'evolution_stage', 'abilities')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'card', 'col_id', 'collection_date')
    search_fields = ('trainer__name', 'card__name', 'col_id', 'collection_date')
