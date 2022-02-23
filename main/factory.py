import factory
from .models import *
from django.contrib.auth.models import User
from faker import Faker


class MjestoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mjesto

    postanski_broj = factory.Faker("numerify")
    naziv_mjesta = factory.Faker("city")
    drazava = factory.Faker("country")


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    naziv_eventa = factory.Faker("sentence")
    datum_odrzavanja = factory.Faker("date")
    opis_eventa = factory.Faker("sentence")
    placanje_ulaza =factory.Faker("boolean")
    vrijeme_odrzavanja = factory.Faker("time")
    cijena_ulaza =factory.Faker("numerify")
    mjesto_odrzavanja = factory.Iterator(Mjesto.objects.all())
    autor_objave = factory.Iterator(User.objects.all())
    adresa = factory.Faker("address")
    #zainteresirani =factory.Faker("numerify")
    #dolaze =factory.Faker("numerify")
    #korisnici = models.ManyToManyField(User, default=None, blank=True)



