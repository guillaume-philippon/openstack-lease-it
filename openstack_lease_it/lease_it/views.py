#!/usr/local/bin/python2.7
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from lease_it.Backend import OpenstackConnection


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def flavors(request):
    openstack = OpenstackConnection()
    response = openstack.usage()
    return JsonResponse(response)
