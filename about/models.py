from django.db import models

class About(models.Model):
    image = models.ImageField(upload_to='images/')
