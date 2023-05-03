from django.db import models
from django.urls import reverse
# Create your models here.
class product(models.Model):
    title   = models.CharField(max_length=120)
    decs   = models.TextField(blank=True, null=True)
    price  = models.DecimalField(decimal_places=2,max_digits=200)
    summry = models.TextField()
    featured = models.BooleanField(default=False )

 