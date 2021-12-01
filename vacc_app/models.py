from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Vac_Centers(models.Model):
  center_name = models.CharField(max_length=100)
  VAC_TYPE = (
    ("P", "Pfizer"),
    ("M", "Moderna")
  )
  vac_type = models.CharField(max_length=100, choices=VAC_TYPE)
  postal_code = models.IntegerField(
    default=1, 
    validators=[
      MinValueValidator(1), 
      MaxValueValidator(999999)
      ])



class Slots(models.Model):
  vac_center = models.ForeignKey(Vac_Centers, on_delete= models.CASCADE)
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
  time_slots = models.CharField(max_length=100, choices=TIME_SLOTS)
  FIRST_OR_SECOND = (
    ('First', 'First jab'),
    ('Second', 'Second jab')
  )
  first_or_second = models.CharField(max_length=100, choices=FIRST_OR_SECOND)
  person_name = models.CharField(max_length=100,)
  person_nric = models.CharField(max_length=4, null=True)


class Persons(models.Model):
  user = models.OneToOneField(User, on_delete=models.PROTECT)
  JAB_DONE = (
    ('None', 'None'),
    ('First done', 'First done'),
    ('Second done', 'Second done')
  )
  jab_done = models.CharField(max_length=100, choices=JAB_DONE)
  