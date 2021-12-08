from django.db import models
from django.db.models.deletion import CASCADE



class Mjesto(models.Model):
    postanski_broj = models.IntegerField()
    naziv_mjesta = models.CharField(max_length = 50)
    mjesto = models.CharField(max_length = 50)

    def __str__(self):
        return self.naziv_mjesta

class AdminKorisnici(models.Model):
    adresa_ustanove = models.CharField(max_length = 150)
    naziv_admina = models.CharField(max_length = 50)
    kontakt_admina = models.IntegerField()
    mjesto = models.ForeignKey(Mjesto, on_delete=CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.naziv_admina

class Objava(models.Model):
    naslov_objave = models.CharField(max_length = 100)
    vrijeme_objave = models.DateTimeField()
    datum_objave = models.DateTimeField()
    opis_objave = models.CharField(max_length = 500)
    autor_objave = models.ForeignKey(AdminKorisnici, on_delete=CASCADE, default=None, blank=True, null=True)
    

    def __str__(self):
        return self.naslov_objave

class Event(models.Model):
    naziv_eventa = models.CharField(max_length = 100)
    datum_odrzavanja = models.DateTimeField()
    opis_eventa = models.CharField(max_length = 500)
    placanje_ulaza = models.BooleanField()
    vrijeme_odrzavanja = models.DateTimeField()
    cijena_ulaza = models.IntegerField()
    mjesto_odrzavanja = models.ForeignKey(Mjesto, on_delete=CASCADE, default=None, blank=True, null=True)
    zainteresirani = models.IntegerField()
    dolaze = models.IntegerField()
    objava = models.ForeignKey(Objava, on_delete=CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.naziv_eventa

class Korisnik(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length=1000)
    eventi = models.ManyToManyField(Event, default=None, blank=True)

    def __str__(self):
        return self.username
