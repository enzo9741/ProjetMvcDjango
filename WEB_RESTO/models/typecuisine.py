from django.db import models

class Typecuisine(models.Model):
    idtc = models.BigIntegerField(db_column='idTC', primary_key=True)  # Field name made lowercase.
    libelletc = models.CharField(db_column='libelleTC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'web_resto_typecuisine'

    def __str__(self):
        return self.libelletc