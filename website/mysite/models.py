from django.db import models

# Create your models here.
#mysite_sampleform

class SampleForm(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name