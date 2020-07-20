from django.contrib import admin
from django.urls import path

from careers.views import MainView, VacanciesView, VacanciesCatView, CompanyView, VacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('vacancies', VacanciesView.as_view()),
    path('vacancies/cat/<str:category>/', VacanciesCatView.as_view()),
    path('companies/<int:id>/', CompanyView.as_view()),
    path('vacancies/<int:id>/', VacancyView.as_view()),
]
