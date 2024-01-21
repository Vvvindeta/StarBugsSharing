from django.db import models

from users.models import User


class Rover(models.Model):
    rover_id = models.AutoField(primary_key=True)
    rover_name = models.CharField(max_length=20)
    rover_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='rovers_images', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    charge = models.PositiveIntegerField(default=0)
    location_id = models.IntegerField()
    equipment = models.TextField(null=True)
    mileage = models.PositiveIntegerField(default=0)
    speed = models.PositiveIntegerField(default=0)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Марсоход'
        verbose_name_plural = 'Марсоходы'
    
    def __str__(self):
        return f"{self.rover_name} {self.rover_number}"
    
    def equipment_as_list(self):
        return list(self.equipment.split(','))


class Using(models.Model):
    using_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', related_name='usings')
    rover = models.ForeignKey(Rover, on_delete=models.CASCADE, db_column='rover_id', related_name='usings')
    
    class Meta:
        verbose_name = 'Аренду'
        verbose_name_plural = 'Аренды'