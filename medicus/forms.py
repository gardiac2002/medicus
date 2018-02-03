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



class ProposeDoctorForm(forms.ModelForm):
    class Meta:
        model = medicus_models.Doctor
        fields = (
            'name',
            'profession',
            'address',
            'phone_number',
            'email',
            'info',
            'picture'
        )


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




