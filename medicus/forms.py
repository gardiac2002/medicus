from django import forms

from medicus import models as medicus_models

# class DoctorFilterForm(forms.Form):
#     city = forms.CharField(required=True, max_length=100)
#     name_or_profession = forms.CharField(required=False, max_length=100)
#
#

class SearchDoctorForm(forms.Form):
    """
    Search a doctor on the website.
    """
    profession = forms.CharField(label='profession', max_length=120)
    city = forms.CharField(required=True, label='city', max_length=120)


class ProposeDoctorForm(forms.Form):

    name = forms.CharField(label='name', max_length=128)
    profession = forms.CharField(label='profession', max_length=128)
    address = forms.CharField(label='address', max_length=128)
    city = forms.CharField(label='city', max_length=128)
    telephone = forms.CharField(label='telephone', max_length=64)
    email = forms.EmailField(required=False, label='email', max_length=128)
    website = forms.URLField(required=False, label='website', max_length=128)



class NewRatingForm(forms.ModelForm):

    class Meta:
        model = medicus_models.Rating
        fields = (
            'doctor',
            'user',

            'treatment',
            'empathy',
            'price',
            'waiting_time',

            'comment',
        )




