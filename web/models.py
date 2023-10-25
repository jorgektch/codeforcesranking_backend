from django.db import models

class Member(models.Model):
    position = models.IntegerField(default = 0)
    name = models.CharField(max_length = 50)
    handle = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    rating = models.IntegerField(default = 0)
