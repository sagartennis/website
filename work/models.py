from django.db import models

class Work(models.Model):
    images = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)


    def __str__(self):
        return self.title
