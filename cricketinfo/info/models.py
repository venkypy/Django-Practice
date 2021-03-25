from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=250, unique=True)
    flag = models.ImageField(blank=True, null=True)
    shortname = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=250, default="about your country")

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    hs = models.IntegerField(blank=True,default=True)

def dob_validate(dob_date):
    print("*"*20)
    print(dob_date)

class Player2(models.Model):
    specials = [("bm","Batsman"), ("bl","Bowler"), ("kp","Keeper"), ("al","Alrounder")]
    name = models.CharField(max_length=250, unique=True)
    dob = models.DateField(validators=[dob_validate])
    special = models.CharField(choices=specials, max_length=3)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


