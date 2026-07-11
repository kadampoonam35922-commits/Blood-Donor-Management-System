from django.db import models

class Donor(models.Model):

    name = models.CharField(max_length=100)

    gender = models.CharField(max_length=20)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    blood = models.CharField(max_length=10)

    state = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    password = models.CharField(max_length=100)