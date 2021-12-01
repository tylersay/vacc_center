from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class vac_Center(models.Model):
  center_name = models.CharField(max_length=100)
  VAC_TYPE = (
    ("P", "Pfizer"),
    ("M", "Moderna")
  )
  vac_type = models.CharField(choices=VAC_TYPE)
  postal_code = models.IntegerField(
    default=1, 
    validators=[
      MinValueValidator(1), 
      MaxValueValidator(999999)
      ])



class slots(models.Model):
  vac_center = models.ForeignKey(vac_Center, on_delete= models.CASCADE)
  date_assigned = models.DateField()
  TIME_SLOTS = (
    ('9am', '9am'),
    ('10am', '10am'),
    ('11am', '11am'),
    ('12am', '12am'),
    ('1pm', '1pm'),
    ('2pm', '2pm'),
    ('3pm', '3pm'),
    ('4pm', '4pm')   
  )
  time_slots = models.CharField(choices=TIME_SLOTS)
  FIRST_OR_SECOND = (
    ('First', 'First jab'),
    ('Second', 'Second jab')
  )
  first_or_second = models.CharField(choices=FIRST_OR_SECOND)
  person_name = models.CharField(max_length=100)
  person_nric = models.CharField(max_length=4)

  