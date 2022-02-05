from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator



class Mjesto(models.Model):
    postanski_broj = models.IntegerField(validators=[MinValueValidator(0)])
    naziv_mjesta = models.CharField(max_length = 50)
    drazava = models.CharField(max_length = 50)

    def __str__(self):
        return self.naziv_mjesta

class AdminKorisnici(models.Model):
    adresa_ustanove = models.CharField(max_length = 150)
    naziv_admina = models.CharField(max_length = 50)
    kontakt_admina = models.CharField(max_length = 20)
    password = models.CharField(max_length=1000)
    mjesto = models.ForeignKey(Mjesto, on_delete=CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.naziv_admina

class Event(models.Model):
    naziv_eventa = models.CharField(max_length = 100)
    datum_odrzavanja = models.DateField()
    opis_eventa = models.CharField(max_length = 500)
    placanje_ulaza = models.BooleanField()
    vrijeme_odrzavanja = models.TimeField()
    cijena_ulaza = models.IntegerField(validators=[MinValueValidator(0)])
    mjesto_odrzavanja = models.ForeignKey(Mjesto, on_delete=CASCADE, default=None, blank=True, null=True)
    zainteresirani = models.IntegerField(validators=[MinValueValidator(0)])
    dolaze = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.naziv_eventa

class Objava(models.Model):
    naslov_objave = models.CharField(max_length = 100)
    vrijeme_objave = models.DateTimeField()
    datum_objave = models.DateTimeField()
    opis_objave = models.CharField(max_length = 500)
    autor_objave = models.ForeignKey(AdminKorisnici, on_delete=CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.naslov_objave

class Korisnik(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length=1000)
    eventi = models.ManyToManyField(Event, default=None, blank=True)

    def __str__(self):
        return self.username
