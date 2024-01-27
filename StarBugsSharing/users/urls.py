from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout, name='logout'),
    path('increase_balance/', views.increase_balance, name='increase_balance'),
]
