from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def swagg(request: HttpRequest, swg_lvl):
    return HttpResponse(f'<h1>Страница свэга</h1><p>Уровень свэга: {swg_lvl}</p>')

def swagg_slug(request: HttpRequest, swg_slug):
    return HttpResponse(f'<h1>Страница свэга</h1><p>Реклама: {swg_slug}</p>')

def popular(request: HttpRequest):
    return HttpResponse('<h1>Mega kek 2000</h1>')

def index(request: HttpRequest):
    return HttpResponse('<h1>Ало бизнесс</h1>')

def history(request: HttpRequest, year):
    return HttpResponse(f'<h1>История свэга</h1><p>Год: {year}</p>')