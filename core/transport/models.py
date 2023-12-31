from django.db import models

class Transport(models.Model):
    name = models.CharField(max_length=50)
    start_place = models.CharField(max_length=50)
    end_place = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    default_temperature = models.FloatField()
    default_humidity = models.FloatField()
    delta_temperature = models.FloatField()
    delta_humidity = models.FloatField()
    freezer_status = models.FloatField()
    nebulizer_status = models.BooleanField()

    def __str__(self):
        return self.name
