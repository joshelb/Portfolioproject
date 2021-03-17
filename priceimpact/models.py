from django.db import models

# Create your models here.
class orderdeltamodel(models.Model):
    qty = models.FloatField()
    buy = models.BooleanField()
    time = models.CharField(max_length=14)
















