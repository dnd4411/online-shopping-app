from django.db import models
from django.contrib.auth.models import User
from store.models.customer import Customer

class userotp(models.Model):
    time_st=models.DateField(auto_now=True)
    otp=models.IntegerField(max_length=10)
