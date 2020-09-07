from django.db import models

class Home(models.Model):
    image = models.ImageField(upload_to='images/')
