from django.db import models

# Create your models here.


class Sports(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    data = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.ForeignKey(Sports, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
