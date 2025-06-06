from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.FourDigitYearConverter, 'year_conv')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('swagg/', views.swagg, name='swg_lvl'),
    path('castle/<int:mbr_id>/', views.castle, name='castle')
]