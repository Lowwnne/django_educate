from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.FourDigitYearConverter, 'year_conv')

urlpatterns = [
    path('', views.index),
    path('swagg/<int:swg_lvl>/', views.swagg_lvl),
    path('swagg/<slug:swg_slug>/', views.swagg_slug),
    path('history/<year_conv:year>/', views.history),
]