from django.urls import path
from django.conf.urls import handler404, handler500

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),

    path('faq/', views.faq, name='faq'),
    path('premium/', views.premium, name='premium'),
    path('rules/', views.rules, name='rules'),
    path('rent/', views.rent, name='rent')
]

handler404 = 'main.views.error_404'
# handler500 = 'main.views.error_500'