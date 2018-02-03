from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader



def index(request):
    """

    :param request:
    :return:
    """
    template = loader.get_template('medicus/index.html')
    return HttpResponse(template.render({}, request))


def listing(request):
    template = loader.get_template('medicus/listing.html')
    return HttpResponse(template.render({}, request))