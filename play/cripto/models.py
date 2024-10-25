from django.db import models

# Create your models here.
client = models.CharField(max_length=225)
send_amout = models.CharField(max_length=225)
get_amout = models.CharField(max_length=225)
get_currency = models.FloatField()
send_currency = models.FloatField()