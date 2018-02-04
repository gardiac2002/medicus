# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from os import path, listdir

from medicus.settings.production import DATA_ROOT
from medicus import models


def prepopulate_data():
    for file in listdir(DATA_ROOT):
        city_name = file.split('.')[0]
        # import ipdb
        # ipdb.set_trace()
        # Create city and country
        country, _ = models.Country.objects.get_or_create(name='Rumania')
        city, _ = models.City.objects.get_or_create(name=city_name.capitalize())

        f_path = path.join(DATA_ROOT, file)
        data = []
        with open(f_path, 'r') as f:
            for line in f:
                data.append(eval(line.strip()))

        for d in data:
            profession, _ = models.Profession.objects.get_or_create(name=d['speciality'].strip())

            if d['address'].lower().strip() == 'n/a':
                address = ''
            elif isinstance(d['address'], str):
                address = d['address']
            else:
                address = ''

            phone = d['phone'].strip() or ''

            doctor = models.Doctor(
                name=d['name'].strip(),
                profession=profession,
                street=address,
                city=city,
                phone_number=phone,
            )

            doctor.full_clean()
            doctor.save()


def load_doctors(apps, schema_editor):
    prepopulate_data()


def delete_doctors(apps, schema_editor):
    models.Country.objects.all().delete()
    models.Profession.objects.all().delete()
    models.City.objects.all().delete()
    models.address.objects.all().delete()
    models.Doctor.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('medicus', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(load_doctors, delete_doctors),
    ]