# -*- coding: utf-8 -*-
# pylint: skip-file
"""
TestConnection is a module of Fake backend used to help developpement
of API
"""
from django.utils.dateparse import parse_datetime
from django.core.cache import cache
from django.utils import timezone

from dateutil.relativedelta import relativedelta

from lease_it.backend.OpenstackConnection import OpenstackConnection, INSTANCES_CACHE_TIMEOUT,\
    PROJECTS_CACHE_TIMEOUT, USERS_CACHE_TIMEOUT, FLAVOR_CACHE_TIMEOUT
from lease_it.backend.Exceptions import PermissionDenied


class TestConnection(OpenstackConnection):
    """
    This class is only used for developement. This will
    return false value formated as expected by views.
    """
    def __init__(self):
        self.session = None

    def _instances(self):
        """
        Return some fake value for _instances. OpenstackConnection return
        the same kind of values
        :return: dict()
        """
        response = cache.get('instances')
        if not response:
            response = {
                'instance-01': {
                        'user_id': 1,
                        'project_id': 'project-01',
                        'id': 'instance-01',
                        'name': 'instance-name-01',
                        'created_at': timezone.now().date() + relativedelta(days=-300)
                    },
                'instance-02': {
                    'user_id': 1,
                    'project_id': 'project-01',
                    'id': 'instance-02',
                    'name': 'instance-name-02',
                    'created_at': timezone.now().date() + relativedelta(days=-30)
                },
                'instance-03': {
                    'user_id': 2,
                    'project_id': 'project-01',
                    'id': 'instance-03',
                    'name': 'instance-name-03',
                    'created_at': timezone.now().date() + relativedelta(days=-30)
                },
                'instance-04': {
                    'user_id': 2,
                    'project_id': 'project-01',
                    'id': 'instance-04',
                    'name': 'instance-name-04',
                    'created_at': timezone.now().date() + relativedelta(days=-30)
                },
                'instance-05': {
                    'user_id': 1,
                    'project_id': 'project-01',
                    'id': 'instance-05',
                    'name': 'instance-name-05',
                    'created_at': timezone.now().date() + relativedelta(days=-30)
                },
            }
            cache.set('instances', response, INSTANCES_CACHE_TIMEOUT)
        return response

    def _flavors(self):
        """
        Return some fake value for _instances. OpenstackConnection return
        the same kind of values
        :return: dict()
        """
        response = cache.get('flavors')
        if not response:
            response = {
                'flavor.01': {
                    'name': 'flavor.01',
                    'disk': 20,
                    'ram': 1024,
                    'cpu': 1
                },
                'flavor.02': {
                    'name': 'flavor.02',
                    'disk': 20,
                    'ram': 2048,
                    'cpu': 2
                }
            }
            cache.set('flavors', response, 0)
        return response

    def _hypervisors(self):
        """
        Return some fake value for _instances. OpenstackConnection return
        the same kind of values
        :return: dict()
        """
        return [{
                'status': 'enabled',
                'state': 'up',
                'vcpus': 48,
                'vcpus_used': 60,
                'free_ram': 1024,
                'memory': 102400,
                'free_disk': 2000,
                'local_disk': 4000
            }, {
                'status': 'enabled',
                'state': 'up',
                'vcpus': 48,
                'vcpus_used': 0,
                'free_ram': 102400,
                'memory': 102400,
                'free_disk': 2000,
                'local_disk': 4000
            }]

    def _domains(self):
        """
        Return some fake value for _instances. OpenstackConnection return
        the same kind of values
        :return: dict()
        """
        response = cache.get('domains')
        if not response:
            response = {
                'domain-01': {
                    'id': 'domain-01',
                    'name': 'domain-name-01'
                },
                'domain-02': {
                    'id': 'domain-02',
                    'name': 'domain-name-02'
                },
            }
            cache.set('domain', response, USERS_CACHE_TIMEOUT)
        return response

    def _users(self):
        """
        Return some fake value for _instances. OpenstackConnection return
        the same kind of values
        :return: dict()
        """
        response = cache.get('users')
        if not response:
            response = {
                1: {
                    'id': 1,
                    'domain_id': 'domain-01',
                    'name': 'John.Doe',
                    'email': 'john.doe'
                },
                2: {
                    'id': 2,
                    'domain_id': 'domain-id-02',
                    'name': 'Jane.Smith is have a very long #name',
                    'email': 'jane.smith@full.domain.com'
                },
            }
            cache.set('users', response, USERS_CACHE_TIMEOUT)
        return response

    def _projects(self):
        """
        Return some fake value for _instances. OpenstackConnection return
        the same kind of values
        :return: dict()
        """
        return dict()