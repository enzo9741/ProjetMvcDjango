from django.db import models

class Photo(models.Model):
    idP = models.BigIntegerField(db_column='idP', primary_key=True)  # Field name made lowercase.
    cheminP = models.CharField(db_column='cheminP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idR = models.ForeignKey('Resto', models.DO_NOTHING, db_column='idR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'web_resto_photo'

    def __str__(self):
        return self.idP