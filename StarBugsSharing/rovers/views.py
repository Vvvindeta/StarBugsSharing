from django.shortcuts import render

from rovers.models import Rover


def rent(request):
    # Получаем список марсоходов
    rovers = Rover.objects.all()
    # Получаем параметры сортировки из запроса
    sort_by = request.GET.get('sort_by', 'default')
    if sort_by == 'rate':
        rovers = rovers.order_by('rate')
    elif sort_by == 'mileage':
        rovers = rovers.order_by('mileage')
    elif sort_by == 'speed':
        rovers = rovers.order_by('speed')

    context = {
        'rovers': rovers,
    }
    return render(request, 'rovers/rent.html', context)
