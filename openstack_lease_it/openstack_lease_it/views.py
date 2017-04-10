#!/usr/local/bin/python2.7
# -*- encoding: utf-8 -*-

import json.tool
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from openstack_lease_it.settings import GLOBAL_CONFIG
from lease_it.Backend import OpenstackConnection
import openstack_auth
import time
import django.views.decorators.vary


def hypervisor_dispatcher(request):
    if 'format' in request.GET and request.GET['format'] == 'json':
        return hypervisor_get_json(request)
    else:
        return hypervisor_get_html(request)


@login_required()
def hypervisor_get_html(request):
    """

    :param request:
    :return:
    """
    return render(request, 'hypervisor_get_html.html')


@login_required()
def hypervisor_get_json(request):
    """

    :param request:
    :return:
    """
    data = {}
    list = []
    con = OpenstackConnection(GLOBAL_CONFIG)
    hypervisors = con.nova_get_hypervisors()

    for each in hypervisors:
        # print json.dumps(each._info, sort_keys=True, indent=4, separators=(',', ': '))
        list.append({
            'host': each._info['hypervisor_hostname'],
            'id': each._info['id'],
            'state': each._info['state'],
            'status': each._info['status'],
            'free_ram_mb': each._info['free_ram_mb'],
            'free_disk_gb': each._info['free_disk_gb'],
            'vcpus': each._info['vcpus'],
            'vcpus_used': each._info['vcpus_used'],
            'instances': each._info['running_vms'],
        })

    # flavors = con.nova_get_flavors()
    # for each in flavors:
    #     print json.dumps(each._info, sort_keys=True, indent=4, separators=(',', ': '))
    data['list'] = list
    return JsonResponse(data)


def home_dispatcher(request):
    if 'format' in request.GET and request.GET['format'] == 'json':
        return home_get_json(request)
    else:
        return home(request)


@login_required()
def home_get_json(request):
    """

    :param request:
    :return:
    """
    data = {}
    list = []
    con = OpenstackConnection(GLOBAL_CONFIG)
    # if 'test' in request.GET:
    #     test = con.keystone_get_user()
    #     print test

    instances = con.nova_get_instances()

    for each in instances:
        # print json.dumps(each._info, sort_keys=True, indent=4, separators=(',', ': '))
        list.append({
            'name': each._info['name'],
            'owner': each._info['user_id'],
            'status': each._info['status'],
            'project': each._info['tenant_id'],
            'start': each._info['OS-SRV-USG:launched_at']
        })
    data['list'] = list
    return JsonResponse(data)


@login_required()
def home(request):
    """
    :param request: HTTP request
    :return: JSONResponse or HTTP
    """
    # con = OpenstackConnection(GLOBAL_CONFIG)
    # print con.sess

    # instances = con.nova_get_instances()
    # for each in instances:
        # print each._info
        # print json.dumps(each._info, sort_keys=True, indent=4, separators=(',', ': '))
        # print each._info['name']
    return render(request, 'home_get_html.html')

