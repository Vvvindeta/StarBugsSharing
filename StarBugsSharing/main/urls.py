from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/', views.faq, name='faq'),
    path('premium/', views.premium, name='premium'),
    path('rules/', views.rules, name='rules'),
]
