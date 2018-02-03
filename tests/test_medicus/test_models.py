from django.test import TestCase

from medicus import models as medi_models


class TestRating(TestCase):
    def test_000_new_rating(self):
        country = medi_models.Country.objects.create(name='Rumania')
        province = medi_models.Province.objects.create(country=country, name='bla')
        postal_code = medi_models.PostalCode.objects.create(postal_code=1234)
        city = medi_models.City.objects.create(postal_code=postal_code, country=country, province=province, name='some city')

        address = medi_models.Address.objects.create(
            city=city,

            country=country,
            street='some_street',
            house_number='123'
        )

        profession = medi_models.Profession.objects.create(name='bla')

        doc = medi_models.Doctor.objects.create(name='dr. alibert', address=address, profession=profession)

        rating = medi_models.Rating(treatment=1,
                                    empathy=1,
                                    price=1,
                                    waiting_time=1,
                                    doctor=doc)

        rating.full_clean()
        rating.save()

        self.assertEquals(rating.general_score, 1)



