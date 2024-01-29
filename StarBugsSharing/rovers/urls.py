from django.urls import path

from rovers import views

app_name = 'rovers'

urlpatterns = [
    path('rent/', views.rent, name='rent'),
]
