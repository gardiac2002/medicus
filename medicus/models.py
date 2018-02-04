from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PostalCode(models.Model):
    postal_code = models.IntegerField()

    def __str__(self):
        return str(self.postal_code)


class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)
    # district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    # postal_code = models.ForeignKey(PostalCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Location(models.Model):
#     name = models.CharField(max_length=100)
#
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     province = models.ForeignKey(Province, on_delete=models.CASCADE)
#
#     district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
#
#     postal_code = models.OneToOneField(PostalCode, on_delete=models.CASCADE, blank=True, null=True)
#
#     def __str__(self):
#         return self.name


class Address(models.Model):
    name = models.CharField(max_length=200, blank=True, )
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
   # location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    street = models.CharField(max_length=150, blank=True, default='')
    # house_number = models.CharField(max_length=10, blank=True, default='')

    address = models.CharField(max_length=200)

    def __str__(self):
        return str((self.street, self.house_number))


class Profession(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=False)

    profession = models.ForeignKey(Profession, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=120)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True)

    # address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, default='')
    email = models.CharField(max_length=150, blank=True, default='')
    info = models.TextField(blank=True, default='')
    website = models.URLField(blank=True, default='')
    picture = models.ImageField(upload_to='doctor/images', blank=True)

    def __str__(self):
        return str((self.name, self.profession))


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=100, )

    # if a user is also a doctor
    doctor = models.OneToOneField(Doctor, blank=True, null=True, on_delete=models.CASCADE)


class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'insufficient'),
        (2, 'sufficient'),
        (3, 'satisfactory'),
        (4, 'good'),
        (5, 'very good')
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    treatment = models.IntegerField(choices=RATING_CHOICES)
    empathy = models.IntegerField(choices=RATING_CHOICES)
    price = models.IntegerField(choices=RATING_CHOICES)
    waiting_time = models.IntegerField(choices=RATING_CHOICES)

    comment = models.TextField(blank=True, default='')

    @property
    def general_score(self):
        scores = [self.treatment, self.empathy, self.price, self.waiting_time]
        average = sum(scores) / len(scores)

        return average
