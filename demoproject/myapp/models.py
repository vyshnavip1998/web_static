from django.db import models


# Create your models here.


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Meet(models.Model):
    team = models.CharField(max_length=250)
    profile = models.ImageField(upload_to='pics')
    post = models.TextField()

    def __str__(self):
        return self.team

