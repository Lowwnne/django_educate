from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.FourDigitYearConverter, 'year_conv')

urlpatterns = [
    path('', views.index),
    path('history/<year_conv:year>/', views.history),
    path('swagg/<int:swg_lvl>/', views.swagg),
    path('swagg/<str:swg_slug>/', views.swagg_slug),
    path('popular/', views.popular)
]