from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse

artists = [{'id': 1, 'title': 'Kai Angel', 'content': 'say viperr', 'is_published': False},
               {'id': 2, 'title': 'Ivanzolo2004', 'content': 'autism 🤘🤘🤘', 'is_published': True},
               {'id': 3, 'title': 'Платина', 'content': 'Бигбой капиталист', 'is_published': True},
               {'id': 4, 'title': 'Куни вест', 'content': 'черный 👨🏿👨🏿👨🏿', 'is_published': False}]

menu = ['Swagg', 'History', 'About']

def about(request: HttpRequest):
    data = {'title': 'О сайте', 'text': 'Киндер буено'}
    return render(request, 'swagmeme2010/base.html', data)

def swagg_lvl(request: HttpRequest, swg_lvl):
    return HttpResponse(f'<h1>Страница свэга</h1><p>Уровень свэга: {swg_lvl}</p>')

def swagg_slug(request: HttpRequest, swg_slug):
    print(request.GET)
    return HttpResponse(f'<h1>Страница свэга</h1><p>Реклама: {swg_slug}</p>')

def index(request: HttpRequest):
    data = {'title': 'Главная страница',
                'menu': menu,
                'artists': artists}

    return render(request, 'swagmeme2010/index.html', context=data)

def history(request: HttpRequest, year):
    if year > 2025:
        url = reverse('swg_lvl', args=('404', ))
        print(url)
        return redirect(url)

    return HttpResponse(f'<h1>История свэга</h1><p>Год: {year}</p>')

def page_not_found(request: HttpRequest, exception=None):
    return HttpResponseNotFound('<h1>Ошибка 404. Страница не найдена мабой :&lpar;</h1>')