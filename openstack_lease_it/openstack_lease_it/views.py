#!/usr/local/bin/python2.7
# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import auth


def login(request):
    redirect_page = request.GET.get('next', 0)
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(redirect_page)
        else:
            return render(request, "auth/login.html")
    else:
        return render(request, 'auth/login.html')
