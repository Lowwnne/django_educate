from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse

artists = [{'id': 1, 'name': 'Kai Angel', 'text': 'say viperr'},
               {'id': 2, 'name': 'Ivanzolo2004', 'text': 'autism 🤘🤘🤘'},
               {'id': 3, 'name': 'Платина', 'text': 'Бигбой капиталист'},
               {'id': 4, 'name': 'Куни вест', 'text': 'черный'}]

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