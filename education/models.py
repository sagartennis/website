from django.db import models

# Create your models here.
class Education(models.Model):
    school_name = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    body = models.TextField(blank = True)
    image = models.ImageField(upload_to='images/', blank = True)


    def __str__(self):
        return self.school_name




    def start_date_pretty(self):
        return self.start_date.strftime(' %Y')

    def end_date_pretty(self):
        return self.end_date.strftime(' %Y')
