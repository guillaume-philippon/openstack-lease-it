#!/usr/local/bin/python2.7
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from openstack_lease_it.settings import GLOBAL_CONFIG

