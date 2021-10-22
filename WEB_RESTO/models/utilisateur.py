from django.db import models

class Utilisateur(models.Model):
    mailU = models.CharField(db_column='mailU', primary_key=True, max_length=150)  # Field name made lowercase.
    mdpU = models.CharField(db_column='mdpU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pseudoU = models.CharField(db_column='pseudoU', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'web_resto_utilisateur'

    def __str__(self):
        return self.mailU