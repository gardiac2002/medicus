"""medicus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from medicus import views


urlpatterns = [
    path(r'', views.index, name='home'),
    # url(r'^home', views.index),
    url(r'^listing/(?P<profession>\w+)/(?P<city>\w+)', views.doctor_list),

    url(r'^search', views.search),
    url(r'^thanks', views.thanks),
    url(r'^doctor/(?P<doctorid>\d+)', views.doctor),
    # url(r'^doctor/(?P<pk>\d+)/$', view=views.DoctorDetailView.as_view()),
    # url(r'^user/(?P<pk>\d+)/$', view=views.UserDetailView.as_view()),
    url(r'^addadoctor', views.propose_doctor),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^auth/', include('social_django.urls', namespace='social')),

    path('accounts/', include('allauth.urls')),

    # url(r'^settings/$', views.settings, name='settings'),
    # url(r'^settings/password/$', views.password, name='password'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
