from django.db import models

class Resto(models.Model):
    idR = models.IntegerField(primary_key=True)
    nomR = models.CharField(max_length=255)
    numAdrR = models.CharField(max_length=20)
    voieAdrR = models.CharField(max_length=255)
    cpR = models.CharField(max_length=5)
    villeR = models.CharField(max_length=255)
    latitudeDegR = models.FloatField()
    longitudeDegR = models.FloatField()
    descR = models.TextField()
    horairesR = models.TextField()

    def __str__(self):
        return self.nomR
