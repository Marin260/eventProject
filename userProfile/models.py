from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=CASCADE)
    bio = models.CharField(max_length=150, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=150, default='')
    webstranica = models.CharField(max_length=150, default='')
    firma = models.CharField(max_length=150, default='')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        #lower the size of the picture then sve it
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        """
        used when new event form is submited
        redirects to the new created event detail view
        """
        return reverse("profile-detail", kwargs={"username": self.user.username}) 