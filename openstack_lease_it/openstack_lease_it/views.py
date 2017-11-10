#!/usr/local/bin/python2.7
# -*- encoding: utf-8 -*-
"""
View module manage interaction between user and openstack-lease-it. It provide HTTP interface based
on REST good practice.

openstack_lease_it.view only provide core view
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from openstack_lease_it.settings import LOGGER


def login(request):
    """
    Default login view when we not use openstack_auth module for authentication

    :param request: web request
    :return: HTML rendering
    """
    redirect_page = request.GET.get('next', 0)
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            LOGGER.info("User %s is now connected", request.POST['username'])
            return HttpResponseRedirect(redirect_page)
    # return render(request, "auth/login.html")
    return HttpResponseRedirect('/static/angular/home.html')


def logout(request):
    """
    Default page to logout, we redirect to /

    :param request: web request
    :return: HTML rendering
    """
    LOGGER.info("User %s is now disconnected", request.user.username)
    auth.logout(request)
    return HttpResponseRedirect('/')
