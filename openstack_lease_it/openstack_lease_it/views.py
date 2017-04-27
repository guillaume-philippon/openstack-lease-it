#!/usr/local/bin/python2.7
# -*- encoding: utf-8 -*-
"""
This module manage django HTTP response (HTML rendering or JSONResponse)
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth


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
            return HttpResponseRedirect(redirect_page)
    return render(request, "auth/login.html")
