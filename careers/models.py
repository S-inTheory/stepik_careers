from django.db import models
# from datetime import date

# from careers import data


class Company(models.Model):
    name = models.CharField(max_length=30, unique=False, default='')
    location = models.CharField(max_length=20, default='')
    logo = models.TextField(default='')
    description = models.TextField(default='')
    employee_count = models.IntegerField(null=True, default=0)


class Speciality(models.Model):
    code = models.CharField(max_length=15, unique=False, default='')
    title = models.CharField(max_length=25, default='')
    picture = models.TextField(default='')


class Vacancy(models.Model):
    title = models.CharField(max_length=30)
    speciality = models.ForeignKey(Speciality, related_name='vacancies',
                                   on_delete=models.CASCADE, unique=False)
    company = models.ForeignKey(Company, related_name='vacancies',
                                on_delete=models.CASCADE, unique=False)
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateField()


# for title in data.companies:
#     Company.objects.create(name=title['title'])
#
# for unit in data.specialties:
#     Speciality.objects.create(code=unit['code'], title=unit['title'])
#
# for unit in data.jobs:
#     unit_posted = unit['posted'].split('-')
#     speciality = Speciality.objects.get(code=unit['cat'])
#     company = Company.objects.get(name=unit['company'])
#     Vacancy.objects.create(title=unit['title'], speciality=speciality,
#                            company=company, salary_min=unit['salary_from'],
#                            salary_max=unit['salary_to'],
#                            published_at=date(int(unit_posted[0]),
#                                              int(unit_posted[1]),
#                                              int(unit_posted[2])),
#                            description=unit['desc'])
