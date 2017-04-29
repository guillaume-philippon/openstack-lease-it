#!/usr/local/bin/python2.7
"""
View for app specific url
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from lease_it import Backend
from openstack_lease_it.settings import GLOBAL_CONFIG


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
    # We load BackendConnection from GLOBAL_CONFIG['BACKEND_PLUGIN']
    backend_plugin = getattr(Backend, "{0}Connection".format(GLOBAL_CONFIG['BACKEND_PLUGIN']))

    # We create the object from backend. Be sure that all backend have same methods
    backend = backend_plugin()  # pylint: disable=not-callable

    # We call our method
    response = backend.flavors()
    return JsonResponse(response)
