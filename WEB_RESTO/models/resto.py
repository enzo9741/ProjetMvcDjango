from django.db import models

class Resto(models.Model):
    idR = models.BigIntegerField(db_column='idR', primary_key=True)  # Field name made lowercase.
    nomR = models.CharField(db_column='nomR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numAdrR = models.CharField(db_column='numAdrR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    voieAdrR = models.CharField(db_column='voieAdrR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpR = models.CharField(db_column='cpR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    villeR = models.CharField(db_column='villeR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitudeDegR = models.FloatField(db_column='latitudeDegR', blank=True, null=True)  # Field name made lowercase.
    longitudeDegR = models.FloatField(db_column='longitudeDegR', blank=True, null=True)  # Field name made lowercase.
    descR = models.TextField(db_column='descR', blank=True, null=True)  # Field name made lowercase.
    horairesR = models.TextField(db_column='horairesR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'web_resto_resto'

    def __str__(self):
        return self.nomR