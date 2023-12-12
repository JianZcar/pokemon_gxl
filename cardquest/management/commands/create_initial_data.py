from django.core.management.base import BaseCommand
from cardquest.models import Trainer, PokemonCard, Collection
from datetime import datetime


class Command(BaseCommand):
    help = 'Create initial data'

    def handle(self, *args, **options):
        # Pokemon cards and assign them to variables
        card1 = PokemonCard.objects.create(name="Pikachu", rarity="Rare",hp=60, card_type="Electric", attack="Thunder Shock",
                        description="A mouse-like pokemon that can generate electricity.",
                        weakness="Ground", card_number=25, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Static")

        card2 = PokemonCard.objects.create(name="Charizard", rarity="Legendary",hp=120, card_type="Fire", attack="Flamethrower",
                        description="A dragon-like pokemon that can breathe fire.",
                        weakness="Water", card_number=6, release_date="1996-02-27", evolution_stage="Stage 2",
                        abilities="Blaze")
        card3 = PokemonCard.objects.create(name="Bulbasaur", rarity="Common",hp=60, card_type="Grass", attack="Vine Whip",
                        description="A frog-like pokemon that can use vines to attack.",
                        weakness="Fire", card_number=1, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Overgrow")
        card4 = PokemonCard.objects.create(name="Squirtle", rarity="Common",hp=60, card_type="Water", attack="Bubble",
                        description="A turtle-like pokemon that can shoot water from its mouth.",
                        weakness="Electric", card_number=7, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Torrent")
        card5 = PokemonCard.objects.create(name="Pidgey", rarity="Common",hp=40, card_type="Flying", attack="Gust",
                        description="A bird-like pokemon that can fly.",
                        weakness="Electric", card_number=16, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Keen Eye")
        card6 = PokemonCard.objects.create(name="Rattata", rarity="Common",hp=30, card_type="Normal", attack="Tackle",
                        description="A rat-like pokemon that can run fast.",
                        weakness="Fighting", card_number=19, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Run Away")
        card7 = PokemonCard.objects.create(name="Nidoran", rarity="Common",hp=40, card_type="Poison", attack="Poison Sting",
                        description="A rabbit-like pokemon that can poison its enemies.",
                        weakness="Psychic", card_number=29, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Poison Point")
        card8 = PokemonCard.objects.create(name="Clefairy", rarity="Common",hp=40, card_type="Fairy", attack="Pound",
                        description="A fairy-like pokemon that can sing.",
                        weakness="Steel", card_number=35, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Cute Charm")
        card9 = PokemonCard.objects.create(name="Vulpix", rarity="Common",hp=50, card_type="Fire", attack="Ember",
                        description="A fox-like pokemon that can breathe fire.",
                        weakness="Water", card_number=37, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Flash Fire")
        card10 = PokemonCard.objects.create(name="Jigglypuff", rarity="Common",hp=60, card_type="Normal", attack="Pound",
                        description="A balloon-like pokemon that can sing.",
                        weakness="Fighting", card_number=54, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Cute Charm")
        card11 = PokemonCard.objects.create(name="Zubat", rarity="Common",hp=40, card_type="Poison", attack="Leech Life",
                        description="A bat-like pokemon that can fly.",
                        weakness="Psychic", card_number=41, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Inner Focus")
        card12 = PokemonCard.objects.create(name="Oddish", rarity="Common",hp=40, card_type="Grass", attack="Absorb",
                        description="A plant-like pokemon that can poison its enemies.",
                        weakness="Fire", card_number=43, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Chlorophyll")
        card13 = PokemonCard.objects.create(name="Paras", rarity="Common",hp=40, card_type="Bug", attack="Scratch",
                        description="A mushroom-like pokemon that can poison its enemies.",
                        weakness="Fire", card_number=59, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Effect Spore")
        card14 = PokemonCard.objects.create(name="Venonat", rarity="Common",hp=60, card_type="Bug", attack="Tackle",
                        description="A bug-like pokemon that can poison its enemies.",
                        weakness="Fire", card_number=48, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Compound Eyes")
        card15 = PokemonCard.objects.create(name="Diglett", rarity="Common",hp=30, card_type="Ground", attack="Scratch",
                        description="A mole-like pokemon that can dig underground.",
                        weakness="Water", card_number=50, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Sand Veil")
        card16 = PokemonCard.objects.create(name="Meowth", rarity="Common",hp=60, card_type="Normal", attack="Scratch",
                        description="A cat-like pokemon that can run fast.",
                        weakness="Fighting", card_number=56, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Pickup")
        card17 = PokemonCard.objects.create(name="Psyduck", rarity="Common",hp=50, card_type="Water", attack="Scratch",
                        description="A duck-like pokemon that can use psychic powers.",
                        weakness="Electric", card_number=54, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Damp")
        card18 = PokemonCard.objects.create(name="Mankey", rarity="Common",hp=40, card_type="Fighting", attack="Scratch",
                        description="A monkey-like pokemon that can run fast.",
                        weakness="Psychic", card_number=56, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Vital Spirit")
        card19 = PokemonCard.objects.create(name="Growlithe", rarity="Common",hp=60, card_type="Fire", attack="Ember",
                        description="A dog-like pokemon that can breathe fire.",
                        weakness="Water", card_number=58, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Flash Fire")
        card20 = PokemonCard.objects.create(name="Poliwag", rarity="Common",hp=40, card_type="Water", attack="Water Gun",
                        description="A tadpole-like pokemon that can swim.",
                        weakness="Electric", card_number=59, release_date="1996-02-27", evolution_stage="Basic",
                        abilities="Water Absorb")

        trainer1 = Trainer.objects.create(name="Ash", birthdate= "1987-05-22",location= "Pallet Town",email= "ash@pokemon.com")
        trainer2 = Trainer.objects.create(name="Misty", birthdate= "1988-05-22",location= "Cerulean City",email= "misty@pokemon.com")
        trainer3 = Trainer.objects.create(name="Brock", birthdate= "1986-05-22",location= "Pewter City",email= "brock@pokemon.com")
        trainer4 = Trainer.objects.create(name="Gary", birthdate= "1987-05-22",location= "Pallet Town",email= "gary@pokemon.com")
        trainer5 = Trainer.objects.create(name="Jessie", birthdate= "1988-05-22",location= "Viridian City",email= "jessie@pokemon.com")
        trainer6 = Trainer.objects.create(name="James", birthdate= "1986-05-22",location= "Viridian City",email= "james@pokemon.com")
        trainer7 = Trainer.objects.create(name="Mewtwo", birthdate= "1987-05-22",location= "Unknown",email= "mewtwo@pokemon.com")
        trainer8 = Trainer.objects.create(name="Mew", birthdate= "1988-05-22",location= "Unknown",email= "mew@pokemon.com")
        trainer9 = Trainer.objects.create(name="Professor Oak", birthdate= "1986-05-22",location= "Pallet Town",email= "oak@pokemon.com")
        trainer10 = Trainer.objects.create(name="Nurse Joy", birthdate= "1987-05-22",location= "Pallet Town",email= "joy@pokemon.com")

        add_cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11,
                     card12, card13, card14, card15, card16, card17, card18, card19, card20]

        for card in add_cards:
            card.save()

        add_trainers = [trainer1, trainer2, trainer3, trainer4, trainer5, trainer6, trainer7, trainer8, trainer9,
                        trainer10]

        for trainer in add_trainers:
            trainer.save()

        for i in range(1, 6):
            Collection.objects.create(
                trainer=Trainer.objects.get(pk=i),
                card=PokemonCard.objects.get(pk=i),
                col_id=i,
                collection_date=datetime.now()
            )

        self.stdout.write(self.style.SUCCESS('Successfully created initial data'))
