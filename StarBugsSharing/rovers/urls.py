from django.urls import path

from rovers import views

app_name = 'rovers'

urlpatterns = [
    path('rent/', views.rent, name='rent'),
    path('rent-rover/<int:rover_id>/', views.rent_rover, name='rent_rover'),
    path('end-rent/<int:rover_id>/', views.end_rent, name='end_rent')
]
