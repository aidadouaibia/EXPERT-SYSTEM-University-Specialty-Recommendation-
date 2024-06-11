from django.db import models

class UserInput(models.Model):
    Filiere= models.CharField(max_length=100)
    MatierePref = models.CharField(max_length=100)
   