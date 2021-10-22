from django.db import models

class Proposer(models.Model):
    idR = models.OneToOneField('Resto', models.DO_NOTHING, db_column='idR', primary_key=True)  # Field name made lowercase.
    idTC = models.ForeignKey('Typecuisine', models.DO_NOTHING, db_column='idTC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'web_resto_proposer'
        unique_together = (('idR', 'idTC'),)