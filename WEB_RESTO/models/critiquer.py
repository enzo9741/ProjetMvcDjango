from django.db import models

class Critiquer(models.Model):
    idR = models.OneToOneField('Resto', models.DO_NOTHING, db_column='idR', primary_key=True)  # Field name made lowercase.
    mailU = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='mailU')  # Field name made lowercase.
    note = models.IntegerField(blank=True, null=True)
    commentaire = models.CharField(max_length=4096, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_resto_critiquer'
        unique_together = (('idR', 'mailU'),)

    def __str__(self):
        return self.mailU