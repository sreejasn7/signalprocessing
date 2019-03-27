from django.db import models

# Create your models here.



class Measurements(models.Model):

    name = models.CharField(max_length=255, null=False)
    no = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.no)


class Detail_measurements(models.Model):
    size = models.IntegerField(null= False)
    width = models.FloatField(null = False)
    area = models.FloatField(null = False)
