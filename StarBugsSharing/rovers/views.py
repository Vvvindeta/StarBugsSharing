from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta, timezone
import decimal

from rovers.models import Rover, Using
from users.models import User


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
        rovers = rovers.order_by('-speed')

    context = {
        'rovers': rovers,
    }
    return render(request, 'rovers/rent.html', context)

@login_required
def rent_rover(request, rover_id):
    if request.method == 'POST':
        rover = Rover.objects.get(rover_id=rover_id)
        rover.is_available = False
        new_using = Using(
            start_time=datetime.now(),
            user=request.user,
            rover=rover
        )
        new_using.save()
        rover.save()
        messages.success(request, f'Марсоход {rover} успешно арендован!')
        return redirect('rovers:rent')
    else:
        return redirect('rovers:rent')


@login_required
def end_rent(request, rover_id):
    if request.method == 'POST':
        user = request.user
        rover = Rover.objects.get(rover_id=rover_id)
        using = Using.objects.filter(user=user, rover=rover).last()
        using.end_time = datetime.now(timezone(timedelta(hours=3)))
        rover.is_available = True
        using.total = round(float(rover.rate) * (using.end_time - using.start_time).total_seconds() / 60, 2)
        user.balance_value -= decimal.Decimal(using.total)
        user.save()
        rover.save()
        using.save()
        return redirect('users:account')
    else:
        return redirect('users:account')