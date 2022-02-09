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

class AdminKorisniciFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AdminKorisnici

    adresa_ustanove = factory.Faker("address")
    naziv_admina = factory.Faker("company")
    kontakt_admina =factory.Faker("numerify")
    mjesto = factory.Iterator(Mjesto.objects.all())

class ObjavaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Objava

    naslov_objave = factory.Faker("paragraph")
    vrijeme_objave = factory.Faker("date_time")
    datum_objave = factory.Faker("date_time")
    opis_objave = factory.Faker("paragraph")
    autor_objave = factory.Iterator(AdminKorisnici.objects.all())

fake = Faker()
text = fake.words(nb=200)
text = ' '.join([word for word in text])


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    naziv_eventa = title
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



