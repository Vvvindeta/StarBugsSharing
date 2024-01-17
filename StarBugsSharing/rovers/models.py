from django.db import models

class Rover(models.Model):
    rover_id = models.AutoField(primary_key=True)
    rover_number = models.IntegerField()
    image = models.ImageField(upload_to='rovers_images', blank=True, null=True)
    availability = models.BooleanField()
    charge = models.IntegerField()
    location_id = models.IntegerField()
