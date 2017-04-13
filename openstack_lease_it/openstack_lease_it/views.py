#!/usr/local/bin/python2.7
# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from lease_it.Backend import OpenstackConnection


def hypervisor_dispatcher(request):
    if 'format' in request.GET and request.GET['format'] == 'json':
        return hypervisor_get_json(request)
    else:
        return hypervisor_get_html(request)


@login_required()
def hypervisor_get_html(request):
    return render(request, 'hypervisor_get_html.html')


@login_required()
def hypervisor_get_json(request):
    response = dict()
    response['list'] = list()
    openstack = OpenstackConnection()
    os_hypervisors = openstack.hypervisors()

    for hypervisor in os_hypervisors:
        response['list'].append({
            'host': hypervisor._info['hypervisor_hostname'],
            'id': hypervisor._info['id'],
            'state': hypervisor._info['state'],
            'status': hypervisor._info['status'],
            'free_ram_mb': hypervisor._info['free_ram_mb'],
            'free_disk_gb': hypervisor._info['free_disk_gb'],
            'vcpus': hypervisor._info['vcpus'],
            'vcpus_used': hypervisor._info['vcpus_used'],
            'instances': hypervisor._info['running_vms'],
        })
    return JsonResponse(response)


def home_dispatcher(request):
    if 'format' in request.GET and request.GET['format'] == 'json':
        return home_get_json(request)
    else:
        return home(request)


@login_required()
def home_get_json(request):
    response = dict()
    instances = list()
    openstack = OpenstackConnection()
    os_instances = openstack.instances()

    for instance in os_instances:
        instances.append({
            'name': instance._info['name'],
            'owner': instance._info['user_id'],
            'status': instance._info['status'],
            'project': instance._info['tenant_id'],
            'start': instance._info['OS-SRV-USG:launched_at']
        })
    response['list'] = instances
    return JsonResponse(response)


@login_required()
def home(request):
    return render(request, 'home_get_html.html')
