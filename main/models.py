from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


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
    date_posted = models.DateTimeField(default=timezone.now)
    naziv_eventa = models.CharField(max_length = 100)
    datum_odrzavanja = models.DateField()
    opis_eventa = models.CharField(max_length = 500)
    placanje_ulaza = models.BooleanField()
    vrijeme_odrzavanja = models.TimeField()
    cijena_ulaza = models.IntegerField(validators=[MinValueValidator(0)])
    mjesto_odrzavanja = models.ForeignKey(Mjesto, on_delete=CASCADE, default=None, blank=True, null=True)
    zainteresirani = models.ManyToManyField(User, default=None, blank=True, related_name="zainteresirani")
    broj_zainteresiranih = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    dolaze = models.ManyToManyField(User, default=None, blank=True, related_name="dolaze")
    broj_dolaze = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    #korisnici = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return self.naziv_eventa


    def countDolaze(self):
        """
        return the count of users attending the event
        """
        return self.dolaze.all().count()
    
    def countZainteresirani(self):
        """
        return the count of users intrested in attending the event
        """
        return self.zainteresirani.all().count()


class Objava(models.Model):
    naslov_objave = models.CharField(max_length = 100)
    vrijeme_objave = models.DateTimeField()
    datum_objave = models.DateTimeField()
    opis_objave = models.CharField(max_length = 500)
    autor_objave = models.ForeignKey(AdminKorisnici, on_delete=CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.naslov_objave


