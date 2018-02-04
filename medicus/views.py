
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from medicus import forms as medicus_forms
from medicus import models


@login_required
def index(request):
    """

    :param request:
    :return:
    """
    professions = list(models.Profession.objects.values_list('name', flat=True))
    form = medicus_forms.SearchDoctorForm()
    data = {
        'form': form,
        'professions': professions,
    }
    return render(request, 'medicus/index.html', data)


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


def doctor(request, doctorid):

    if request.method == 'GET':
        doctor_obj = models.Doctor.objects.get(pk=doctorid)
        return render(request, 'medicus/doctor.html', {'doctor': doctor_obj})


def doctor_list(request, city, profession):
    if request.method == 'GET':
        city_obj = models.City.objects.get(name=city)
        profession_obj = models.Profession.objects.get(name=profession)
        doctors = models.Doctor.objects.filter(city=city_obj, profession=profession_obj)

        data = {
            'city': city,
            'doctors': doctors
        }
        return render(request,
                      'medicus/listing.html',
                      data)


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
            professions = list(models.Profession.objects.values_list('name', flat=True))
            data = {
                'form': form,
                'professions': professions,
            }
            return render(request, 'medicus/proposedoctor.html', data)
    else:
        professions = list(models.Profession.objects.values_list('name', flat=True))
        return render(request, 'medicus/proposedoctor.html', {'professions': professions})


def thanks(request):
    template = loader.get_template('medicus/thanks.html')
    return HttpResponse(template.render({}, request))


# def doctor(request):
#     template = loader.get_template('medicus/doctor.html')
#     return HttpResponse(template.render({}, request))


def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')
