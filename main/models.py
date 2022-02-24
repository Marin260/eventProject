from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from slugify import slugify
from PIL import Image



class Mjesto(models.Model):
    postanski_broj = models.IntegerField(validators=[MinValueValidator(0)])
    naziv_mjesta = models.CharField(max_length = 50)
    drazava = models.CharField(max_length = 50)

    def __str__(self):
        return self.naziv_mjesta

class Event(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    naziv_eventa = models.CharField(max_length = 100)
    opis_eventa = models.TextField()
    datum_odrzavanja = models.DateField()
    vrijeme_odrzavanja = models.TimeField()
    placanje_ulaza = models.BooleanField()
    cijena_ulaza = models.IntegerField(validators=[MinValueValidator(0)])
    mjesto_odrzavanja = models.ForeignKey(Mjesto, on_delete=CASCADE, default=None, blank=True, null=True)
    adresa = models.CharField(max_length=100, default='')
    slika = models.ImageField(default='default_event.jpg', upload_to='event_pics')
    zainteresirani = models.ManyToManyField(User, default=None, blank=True, related_name="zainteresirani")
    broj_zainteresiranih = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    dolaze = models.ManyToManyField(User, default=None, blank=True, related_name="dolaze")
    broj_dolaze = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    autor_objave = models.ForeignKey(User, on_delete=CASCADE, default=None, blank=True, null=True)

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

    def get_absolute_url(self):
        """
        used when new event form is submited
        redirects to the new created event detail view
        """
        return reverse("event-detail", kwargs={"pk": self.pk, 'slug':slugify(self.naziv_eventa)}) 

    def save(self, *args, **kwargs):
        #lower the size of the picture then sve it
        super().save(*args, **kwargs)
        
        img = Image.open(self.slika.path)

        if img.height > 720 or img.width > 1280:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.slika.path)


