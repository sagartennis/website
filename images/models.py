from django.db import models

class Images(models.Model):
    image = models.ImageField(upload_to='images/',blank=True)
    image2 = models.ImageField(upload_to='images/',blank=True)
    image3 = models.ImageField(upload_to='images/',blank=True)
