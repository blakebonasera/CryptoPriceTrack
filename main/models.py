from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    market_cap = models.FloatField()

    def __str__(self):
        return self.name