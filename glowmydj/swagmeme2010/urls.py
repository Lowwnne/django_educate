from django.urls import path, register_converter
from . import views, convertors

register_converter(convertors.FourDigitYearConverter, 'year_conv')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('swagg/<int:swg_lvl>/', views.swagg_lvl, name='swg_lvl'),
    path('swagg/<slug:swg_slug>/', views.swagg_slug),
    path('history/<year_conv:year>/', views.history),
]