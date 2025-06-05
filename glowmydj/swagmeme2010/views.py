from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404


def swagg_lvl(request: HttpRequest, swg_lvl):
    return HttpResponse(f'<h1>Страница свэга</h1><p>Уровень свэга: {swg_lvl}</p>')

def swagg_slug(request: HttpRequest, swg_slug):
    print(request.GET)
    return HttpResponse(f'<h1>Страница свэга</h1><p>Реклама: {swg_slug}</p>')

def index(request: HttpRequest):
    return HttpResponse('<h1>Ало бизнесс</h1>')

def history(request: HttpRequest, year):
    if year > 2025:
        raise Http404()
    return HttpResponse(f'<h1>История свэга</h1><p>Год: {year}</p>')

def page_not_found(request: HttpRequest, exception=None):
    return HttpResponseNotFound('<h1>Ошибка 404. Страница не найдена мабой :&lpar;</h1>')