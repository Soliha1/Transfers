from django.db import models

from django.core.validators import MinValueValidator
class Country(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name

class Club(models.Model):
    name=models.CharField()
    country=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True )
    logo=models.ImageField(upload_to='clubs')
    president=models.CharField(blank=True, null=True)
    coach=models.CharField(blank=True, null=True)
    found_date=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name=models.CharField()
    club=models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    position=models.CharField()
    number=models.PositiveSmallIntegerField()
    nation=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    age=models.PositiveSmallIntegerField(null=True, blank=True)
    price=models.FloatField(validators=[MinValueValidator(0.0)])
# Create your models here.
