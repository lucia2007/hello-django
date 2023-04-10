from django.db import models

# Create your models here.


class Item(models.Model):
    name: models.CharField = models.CharField(
        max_length=50, null=False, blank=False)
    done: models.BooleanField = models.BooleanField(
        null=False, blank=False, default=False)

    def __str__(self):
        return self.name
