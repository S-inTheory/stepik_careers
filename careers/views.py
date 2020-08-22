from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render
from django.views import View

from careers.models import Company, Speciality, Vacancy


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, r'careers/index.html',
                      {'companies': Company.objects.all(),
                       'specialities': Speciality.objects.all(),
                       })


class VacanciesView(View):

    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        count = Vacancy.objects.all().count()
        return render(request, r'careers/vacancies.html',
                      {'vacancies': vacancies,
                       'title': 'Все вакансии',
                       'count': count
                       }, )


class VacanciesCatView(View):

    def get(self, request, category: str, *args, **kwargs):
        cat = Speciality.objects.all().filter(code=category)
        vacancies = Vacancy.objects.all().filter(speciality=cat[0].id)
        title = cat[0].title
        count = Vacancy.objects.all().filter(speciality=cat[0].id).count()
        return render(request, r'careers/vacancies.html',
                      {'vacancies': vacancies,
                       'title': title,
                       'count': count,
                       })


class VacancyView(View):

    def get(self, request, id: int, *args, **kwargs):
        if id:
            vac = Vacancy.objects.all().filter(id=id)
            comp = Company.objects.all().filter(id=vac[0].id)
            return render(request, r'careers/vacancy.html',
                          {'vacancy': vac[0],
                           'company': comp[0],
                           })
        else:
            raise Http404


class CompanyView(View):

    def get(self, request, id: int, *args, **kwargs):
        comp = Company.objects.all().filter(id=id)
        vacancies = Vacancy.objects.all().filter(company=comp[0].id)
        count = Vacancy.objects.all().filter(company=comp[0].id).count()
        if comp:
            return render(request, r'careers/company.html',
                          {'company': comp[0],
                           'vacancies': vacancies,
                           'count': count,
                           })
        else:
            raise Http404


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы не существует')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера')
