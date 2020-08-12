from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, unique=False, default='')
    location = models.CharField(max_length=20, default='')
    logo = models.TextField(default='')
    description = models.TextField(default='')
    employee_count = models.IntegerField(null=True, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')


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


class Application(models.Model):
    written_username = models.CharField(max_length=30)
    written_phone = models.CharField(max_length=30)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
