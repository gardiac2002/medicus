from os import path, listdir

from medicus.settings.production import DATA_ROOT
from medicus import models


def prepopulate_data():
    for file in listdir(DATA_ROOT):
        city_name = file.split('.')[0]

        # Create city and country
        country, _ = models.Country.objects.get_or_create(name='Rumania')
        city, _ = models.City.objects.get_or_create(name=city_name.capitalize(),
                                                    country=country)

        f_path = path.join(DATA_ROOT, file)
        data = []
        with open(f_path, 'r') as f:
            for line in f:
                data.append(eval(line.strip()))

        for d in data:
            profession, _ = models.Profession.objects.get_or_create(name=d['speciality'].stip())

            if d['address'].lower().strip() == 'n/a':
                address=None
            else:
                address = models.Address.objects.get_or_create(
                    city=city,
                    country=country,
                    name=d['address'].strip()
                )

                address.full_clean()
                address.save()

            phone = d['phone'].strip() or ''

            doctor = models.Doctor(
                name=d['name'].strip(),
                profession=profession,
                address=None,
                phone=phone,
            )

            doctor.full_clean()
            doctor.save()