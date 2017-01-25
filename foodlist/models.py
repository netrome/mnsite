from django.db import models

# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=200)
    time = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    n_portions = models.IntegerField(default=0)

    def __str__(self):
        return self.name
