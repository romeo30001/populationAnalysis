from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('wachstumsraten/', views.growth_rates, name='growth_rates'),
    path('altersverteilung/', views.age_distribution, name='age_distribution'),
    path('geschlechterverhaeltnis/', views.gender_ratio, name='gender_ratio'),

]

