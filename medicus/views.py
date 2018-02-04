
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from social_django.models import UserSocialAuth

from medicus import forms as medicus_forms
from medicus import models


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


# @login_required
# def settings(request):
#     user = request.user
#
#     # try:
#     #     github_login = user.social_auth.get(provider='github')
#     # except UserSocialAuth.DoesNotExist:
#     #     github_login = None
#
#     # try:
#     #     twitter_login = user.social_auth.get(provider='twitter')
#     # except UserSocialAuth.DoesNotExist:
#     #     twitter_login = None
#
#     try:
#         facebook_login = user.social_auth.get(provider='facebook')
#     except UserSocialAuth.DoesNotExist:
#         facebook_login = None
#
#     try:
#         google_login = user.social_auth.get(provider='google-oauth2')
#     except UserSocialAuth.DoesNotExist:
#         google_login = None
#     can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
#
#     return render(request, 'registration/settings.html', {
#         # 'github_login': github_login,
#         # 'twitter_login': twitter_login,
#         'facebook_login': facebook_login,
#         'google_login': google_login,
#         'can_disconnect': can_disconnect
#     })
#
#
# @login_required
# def password(request):
#     if request.user.has_usable_password():
#         PasswordForm = PasswordChangeForm
#     else:
#         PasswordForm = AdminPasswordChangeForm
#
#     if request.method == 'POST':
#         form = PasswordForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordForm(request.user)
#     return render(request, 'registration/password.html', {'form': form})


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
