from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse

artists = [{'id': 1, 'title': 'Kai Angel', 'content': 'say viperr', 'is_published': False, 'listeners': 357777},
               {'id': 2, 'title': 'Ivanzolo2004', 'content': 'autism 🤘🤘🤘', 'is_published': True, 'listeners': 6574733},
               {'id': 3, 'title': 'Платина', 'content': 'Бигбой капиталист', 'is_published': True, 'listeners': 77777777},
               {'id': 4, 'title': 'Куни вест', 'content': 'черный 👨🏿👨🏿👨🏿', 'is_published': False, 'listeners': 4677777}]

menu = [{'name': 'Top players', 'tag': 'swg_lvl'},
        {'name': 'About', 'tag': 'about'}]

def index(request: HttpRequest):
    data = {'title': 'Главная страница',
                'menu': menu,
                'artists': artists}

    return render(request, 'swagmeme2010/index.html', context=data)

def swagg(request: HttpRequest):
    data = {'title': 'Топ исполнителей',
            'artists': sorted([a for a in artists if a['is_published']], key=(lambda x: x['listeners'])),
            'menu': menu}
    return render(request, 'swagmeme2010/swg_lvl.html', context=data)

def castle(request: HttpRequest, mbr_id: int):
    data = {'title': 'Пост о игроке',
            'content': f'id игрока: {mbr_id}',
            'menu': menu}
    return render(request, 'swagmeme2010/base.html', )

def about(request: HttpRequest):
    data = {'title': 'О сайте', 'content': 'Киндер буено',
            'menu': menu}
    return render(request, 'swagmeme2010/base.html', context=data)

def page_not_found(request: HttpRequest, exception=None):
    return HttpResponseNotFound('<h1>Ошибка 404. Страница не найдена мабой :&lpar;</h1>')