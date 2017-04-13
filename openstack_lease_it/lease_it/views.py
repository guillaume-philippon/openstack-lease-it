#!/usr/local/bin/python2.7
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth.decorators import login_required
from lease_it.Backend import OpenstackConnection


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def flavors(request):
    os_connection = OpenstackConnection()
    response = os_connection.usage()
    return JsonResponse(response)
