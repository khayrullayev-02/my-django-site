from django.db import models


class Group(models.Model):
    ism = models.CharField(max_length=255)
    familya = models.CharField(max_length=255)
    images = models.ImageField(upload_to='group/')
    tajriba = models.CharField(max_length=255)
    mutaxasisli = models.CharField(max_length=255)

    def __str__(self):
        return self.ism