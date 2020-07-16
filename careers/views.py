from django.shortcuts import render
from django.views import View
from careers.models import Company, Speciality, Vacancy
from django.http import HttpResponseNotFound, HttpResponseServerError


class MainView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, r'careers\index.html',
                      {'companies': Company.objects.all(),
                       'specialities': Speciality.objects.all(),
                       })


class VacanciesView(View):
    template_name = 'vacancies.html'

    def get(self, request, *args, **kwargs):
        return render(request, r'careers\vacancies.html',
                      {'vacancies': Vacancy.objects.all(),
                       'title': 'Все вакансии',
                       'count': Vacancy.objects.all().count()
                       }, )


class VacanciesCatView(View):
    template_name = 'vacancies.html'

    def get(self, request, category: str, *args, **kwargs):
        cat = Speciality.objects.all().filter(code=category)
        return render(request, r'careers\vacancies.html',
                      {'vacancies': Vacancy.objects.all().filter(speciality=cat[0].id),
                       'title': cat[0].title,
                       'count': Vacancy.objects.all().filter(speciality=cat[0].id).count(),
                       })


class VacancyView(View):
    template_name = 'vacancy.html'

    def get(self, request, id: int, *args, **kwargs):
        vac = Vacancy.objects.all().filter(id=id)
        comp = Company.objects.all().filter(id=vac[0].id)
        return render(request, r'careers\vacancy.html',
                      {'vacancy': vac[0],
                       'company': comp[0],
                       })


class CompanyView(View):
    template_name = 'company.html'

    def get(self, request, id: int, *args, **kwargs):
        comp = Company.objects.all().filter(id=id)
        if comp:
            return render(request, r'careers\company.html',
                          {'company': comp[0],
                           'vacancies':
                               Vacancy.objects.all().filter(company=comp[0].id),
                           'count':
                               Vacancy.objects.all().filter(company=comp[0].id).count(),
                           })
        else:
            return HttpResponseNotFound('Такой страницы не существует')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы не существует')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
