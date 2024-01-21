from django.shortcuts import render

from rovers.models import Rover

def rent(request):

    context = {
        "rovers": Rover.objects.all(),
    }

    return render(request, 'rovers/rent.html', context)