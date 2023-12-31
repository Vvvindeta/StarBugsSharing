from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('faq/', faq, name='faq'),
    path('premium/', premium, name='premium'),
    path('rent/', rent, name='rent'),
    path('rules/', rules, name='rules'),
    path('login/', user_login, name='login'),
    path('registration/', registration, name='registration'),
    path('account/', account, name='account'),
]
