import factory
from factory.django import DjangoModelFactory

from main.models import *

class MjestoFactory(DjangoModelFactory):
    class Meta:
        model = Mjesto

    postanski_broj = factory.Faker("numerify")
    naziv_mjesta = factory.Faker("city")
    mjesto = factory.Faker("city")

class AdminKorisniciFactory(DjangoModelFactory):
    class Meta:
        model = AdminKorisnici

    adresa_ustanove = factory.Faker("address")
    naziv_admina = factory.Faker("company")
    kontakt_admina =factory.Faker("numerify")
    mjesto = factory.Iterator(Mjesto.objects.all())

class ObjavaFactory(DjangoModelFactory):
    class Meta:
        model = Objava

    naslov_objave = factory.Faker("paragraph")
    vrijeme_objave = factory.Faker("date_time")
    datum_objave = factory.Faker("date_time")
    opis_objave = factory.Faker("paragraph")
    autor_objave = factory.Iterator(AdminKorisnici.objects.all())

class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    naziv_eventa = factory.Faker("aba")
    datum_odrzavanja = factory.Faker("date_time")
    opis_eventa = factory.Faker("paragraph")
    placanje_ulaza =factory.Faker("boolean")
    vrijeme_odrzavanja = factory.Faker("date_time")
    cijena_ulaza =factory.Faker("numerify")
    mjesto_odrzavanja = factory.Iterator(Mjesto.objects.all())
    zainteresirani =factory.Faker("numerify")
    dolaze =factory.Faker("numerify")
    objava = factory.Iterator(Objava.objects.all())

class KorisnikFactory(DjangoModelFactory):
    class Meta:
        model = Korisnik

    username = factory.Faker("profile")
    password = factory.Faker("sha256")
    eventi = factory.Iterator(Event.objects.all())

