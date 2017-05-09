#!/usr/local/bin/python2.7
"""
View for app specific url
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from lease_it import Backend
from openstack_lease_it.settings import GLOBAL_CONFIG
from lease_it.Backend import Exceptions as bckExceptions  # pylint: disable=ungrouped-imports

# We load backend specify by configuration file
BACKEND_PLUGIN = getattr(Backend, "{0}Connection".format(GLOBAL_CONFIG['BACKEND_PLUGIN']))
BACKEND = BACKEND_PLUGIN()  # pylint: disable=not-callable


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
    # We call our method
    response = BACKEND.flavors()
    return JsonResponse(response)


@login_required
def instances(request):  #pylint: disable=unused-argument
    """
    View for instances list
    :param request: Web request
    :return: JsonResponse w/ list of instances and details
    """
    response = dict()
    data_instances = BACKEND.instances(request)
    data_users = BACKEND.users()
    data_projects = BACKEND.projects()
    for data_instance in data_instances:
        try:
            project = "{name}".format(
                **data_projects[data_instances[data_instance]['project_id']])
        except KeyError:
            project = data_instances[data_instance]['project_id']

        try:
            user = "{first_name} {last_name}".format(
                **data_users[data_instances[data_instance]['user_id']])
        except KeyError:
            user = data_instances[data_instance]['user_id']
        response[data_instance] = {
            'id': data_instances[data_instance]['id'],
            'name': data_instances[data_instance]['name'],
            'created_at': data_instances[data_instance]['created_at'],
            'lease_end': data_instances[data_instance]['lease_end'],
            'project': project,
            'user': user
        }
    return JsonResponse(response)


@login_required
def instance(request, instance_id):
    """
    This is view used to for a new lease on a specific instance (http://url/instances/instance_id)
    a PermissionDenied exception is raised decided by backend. Mainly if instance is not owned by
    user but see Backend comment.
    :param request: Web request
    :param instance_id: retrieve from url
    :return: JsonResponse
    """
    # By default we concidere a success
    response = {
        'status': 'success'
    }
    try:
        BACKEND.lease_instance(request, instance_id)
    except bckExceptions.PermissionDenied as error:
        response = {
            'status': 'error',
            'message': error.message
        }
    return JsonResponse(response)


@login_required
def users(request):  # pylint: disable=unused-argument
    """
    View for users
    :param request: Web request
    :return: JsonResponse w/ list of users and details
    """
    response = BACKEND.users()
    return JsonResponse(response)
