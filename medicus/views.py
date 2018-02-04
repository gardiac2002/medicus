from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
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

    form = medicus_forms.SearchDoctorForm()
    return render(request, 'medicus/index.html', {'form': form})


def search(request):
    if request.method == 'POST':
        form = medicus_forms.SearchDoctorForm(request.POST)

        if form.is_valid():
            city = form.data.get('city')
            profession = form.data.get('profession')
            link = 'listing/{profession}/{city}/'.format(city=city, profession=profession)
            return HttpResponseRedirect(link)
        else:
            return render(request, 'medicus/index.html', {})
    else:
        return render(request, 'medicus/index.html', {})


def doctor(request):
    return render(request, 'medicus/doctor.html', {})


def doctor_list(request, city, profession):
    if request.method == 'GET':

        return render(request, 'medicus/listing.html', {})




#
# class DoctorListView(ListView):
#     model = models.Doctor
#     template_name = 'medicus/listing.html'
#
#     def get_queryset(self):
#         try:
#             city = self.kwargs['city']
#         except KeyError:
#             raise Http404
#         qs = super().get_queryset()
#
#         qs = qs.filter(address__city__name__iexact=city)
#         return qs
#
#     def get(self, request, city, profession):
#         try:
#             # city = request.data['city']
#             # name_or_profession = request.data.get('name_or_profession')
#
#             # TODO add form validation
#
#             qs = models.Doctor.objects.all().filter(address__city__name__iexact=city)
#             if profession:
#                 try:
#                     professions = models.Profession.objects.get(name=profession)
#                     if professions:
#                         qs = qs.filter(profession__name=professions)
#                 except models.Profession.DoesNotExist:
#                     qs = qs.filter(name__icontains=profession)
#
#             return qs
#
#         except KeyError:
#             msg = 'Please provide a city!'
#             raise Http404(msg)
#
#
# class DoctorDetailView(DetailView):
#     model = models.Doctor
#     template_name = 'medicus/doctor_profile.html'
#
#
# class UserDetailView(DetailView):
#     model = models.User
#     template_name = 'medicus/user_profile.html'


def propose_doctor(request):

    if request.method == 'POST':
        form = medicus_forms.ProposeDoctorForm(request.POST)

        if form.is_valid():
            name = form.data.get('name')
            profession = form.data.get('profession')
            address = form.data.get('address')
            city = form.data.get('city')
            telephone = form.data.get('telephone')
            email = form.data.get('email')
            website = form.data.get('website')

            profession_obj, _ = models.Profession.objects.get_or_create(
                name=profession.lower())
            city_obj, _ = models.City.objects.get_or_create(name=city.lower())

            models.Doctor.objects.create(
                name=name,
                profession=profession_obj,
                city=city_obj,
                street=address,
                phone_number=telephone,
                email=email,
                website=website
            )

            return HttpResponseRedirect('thanks')
        else:
            return render(request, 'medicus/proposedoctor.html', {'form': form})
    else:
        return render(request, 'medicus/proposedoctor.html', {})


def thanks(request):
    template = loader.get_template('medicus/thanks.html')
    return HttpResponse(template.render({}, request))


def doctor(request):
    template = loader.get_template('medicus/doctor.html')
    return HttpResponse(template.render({}, request))
