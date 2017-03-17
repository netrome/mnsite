from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MnList(models.Model):
    # General purpose list
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MnItem(models.Model):
    # Item for list
    list = models.ForeignKey(MnList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

