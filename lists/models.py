from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    friends = models.ManyToManyField(User, related_name="friend_profiles", blank=True)

    def __str__(self):
        return str(self.user)


class MnList(models.Model):
    # General purpose list
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_width = models.ManyToManyField(User, related_name="shared_lists")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MnItem(models.Model):
    # Item for list
    list = models.ForeignKey(MnList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.name

