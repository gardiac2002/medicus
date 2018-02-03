from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse

from medicus import forms as medicus_forms
from medicus import models


def index(request):
    """

    :param request:
    :return:
    """
    template = loader.get_template('medicus/index.html')
    return HttpResponse(template.render({}, request))


# def listing(request):
#     template = loader.get_template('medicus/listing.html')
#     return HttpResponse(template.render({}, request))


class DoctorListView(ListView):
    model = models.Doctor
    template_name = 'medicus/listing.html'

    def get_queryset(self):
        try:
            city = self.kwargs['city']
        except KeyError:
            raise Http404
        qs = super().get_queryset()

        qs = qs.filter(address__city__name__iexact=city)

        return qs

    def post(self, request, *args, **kwargs):
        try:
            city = request.data['city']
            name_or_profession = request.data.get('name_or_profession')

            # TODO add form validation

            qs = models.Doctor.objects.all().filter(address__city__name__iexact=city)
            if name_or_profession:
                try:
                    professions = models.Profession.objects.get(name=name_or_profession)
                    if professions:
                        qs = qs.filter(profession__name=professions)
                except models.Profession.DoesNotExist:
                    qs = qs.filter(name__icontains=name_or_profession)

            return qs

        except KeyError:
            msg = 'Please provide a city!'
            raise Http404(msg)


class DoctorDetailView(DetailView):
    model = models.Doctor
    template_name = 'medicus/doctor_profile.html'


class UserDetailView(DetailView):
    model = models.User
    template_name = 'medicus/user_profile.html'

