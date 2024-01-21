from django.contrib import admin

from rovers.models import Rover, Using


@admin.register(Rover)
class RoverAdmin(admin.ModelAdmin):
    pass


@admin.register(Using)
class UsingAdmin(admin.ModelAdmin):
    pass