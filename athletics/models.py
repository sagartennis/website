from django.db import models

class Athletics(models.Model):
    image = models.ImageField(upload_to='images/')
