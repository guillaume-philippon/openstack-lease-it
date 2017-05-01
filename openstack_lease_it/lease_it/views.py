#!/usr/local/bin/python2.7
"""
View for app specific url
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from lease_it import Backend
from openstack_lease_it.settings import GLOBAL_CONFIG

BACKEND_PLUGIN = getattr(Backend, "{0}Connection".format(GLOBAL_CONFIG['BACKEND_PLUGIN']))
BACKEND = BACKEND_PLUGIN()  # pylint: disable=not-callable


@login_required
def dashboard(request):
    """
    The default dashboard
    :param request: Web request
    :return: HTML Rendering
    """
    return render(request, 'dashboard/dashboard.html')


@login_required
def flavors(request):  # pylint: disable=unused-argument
    """
    View for flavors request
    :param request: Web request
    :return: JsonResponse w/ list of flavor and details values
    """
    # We call our method
    response = BACKEND.flavors()
    return JsonResponse(response)


@login_required
def instances(request):  #pylint: disable=unused-argument
    """
    View for instances list
    :param request: Web request
    :return: JsonResponse w/ list of instances and details
    """
    response = BACKEND.instances(from_cache=True)
    return JsonResponse(response)
