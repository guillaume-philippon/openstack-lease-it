#!/usr/local/bin/python2.7
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from lease_it import Backend
from openstack_lease_it.settings import GLOBAL_CONFIG


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def flavors(request):
    # We load BackendConnection from GLOBAL_CONFIG['BACKEND_PLUGIN']
    backend_plugin = getattr(Backend, "{0}Connection".format(GLOBAL_CONFIG['BACKEND_PLUGIN']))

    # We create the object from backend. Be sure that all backend have same methods
    backend = backend_plugin()

    # We call our method
    response = backend.usage()
    return JsonResponse(response)


@login_required
def instances(request):
    openstack = OpenstackConnection()
    response = openstack.instances(request)
    return JsonResponse(response)
