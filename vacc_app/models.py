from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class vac_Center(models.Model):
  name = models.CharField(max_length=100)
  vac_type = models.CharField(max_length=100)
  postal_code = models.IntegerField(
    default=1, 
    validators=[
      MinValueValidator(1), 
      MaxValueValidator(999999)
      ])

class slots