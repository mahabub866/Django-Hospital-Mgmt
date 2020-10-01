from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    emailid = models.CharField(max_length=30)
    age = models.CharField(max_length=20)
    gender= models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=20)
    unit = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Plan(models.Model):
        name = models.CharField(max_length=30)
        amount = models.CharField(max_length=20)
        duration = models.CharField(max_length=30)
        def __str__(self):
            return self.name


class Member(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    emailid = models.CharField(max_length=30)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    plan = models.CharField(max_length=20)
    joindate = models.CharField(max_length=20)
    expiredate = models.CharField(max_length=20)
    initial = models.CharField(max_length=20)

    def __str__(self):
        return self.name



