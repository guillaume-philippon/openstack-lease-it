# -*- coding: utf-8 -*-
"""
TestConnection is a module of Fake backend used to help developpement
of API
"""
from django.utils.dateparse import parse_datetime
from lease_it.datastore.ModelAccess import InstancesAccess
from lease_it.Backend.Exceptions import PermissionDenied


class TestConnection(object):
    """
    This class is only used for developement. This will
    return false value formated as expected by views.
    """
    @staticmethod
    def users():
        """
        Return a list of fake user with there id, fullname and
        other useful details
        :return: dict()
        """
        response = {
            '1': {
                'id': '1',
                'first_name': 'John',
                'last_name': 'Smith',
                'email': 'john.smith@example.com'
            },
            '2': {
                'id': '2',
                'first_name': 'Jane',
                'last_name': 'Doe',
                'email': 'jane.doe@fake.com'
            },
        }
        return response

    @staticmethod
    def instances(request):  # pylint: disable=unused-argument
        """
        Return a list of fake value for some instances. Each instances
        is must contain owner id, project id, instance id, name of the
        instance, starting date of instance, last time a lease as been put,
        the leasing duration
        :param from_cache: If true, the date will be read from database, if false
                           we retrieve information from backend and update cache database

        :return: dict()
        """
        # Response is a fake dict that provide Backend information. OpenStack backend return
        # should be process to format a dict like it.
        response = {
            '1': {
                'user_id': '1',
                'project_id': '1',
                'id': '1',
                'name': 'user1_project1_expire',
                'created_at': parse_datetime('2017-04-29T17:40:26Z'),
            },
            '2': {
                'user_id': '1',
                'project_id': '1',
                'id': '2',
                'name': 'user1_project1_expire',
                'created_at': parse_datetime('2017-04-29T17:40:26Z'),
            },
            '3': {
                'user_id': '1',
                'project_id': '1',
                'id': '3',
                'name': 'user1_project1_close_to',
                'created_at': parse_datetime('2017-04-29T17:40:26Z'),
            },
            '4': {
                'user_id': '1',
                'project_id': '1',
                'id': '4',
                'name': 'user1_project1_renew',
                'created_at': parse_datetime('2017-04-29T17:40:26Z'),
            },
            '5': {
                'user_id': '1',
                'project_id': '1',
                'id': '5',
                'name': 'user1_project1_long_lease',
                'created_at': parse_datetime('2017-05-01T01:00:00Z'),
            }
        }
        return InstancesAccess.show(response)

    @staticmethod
    def flavors():
        """
        Return a list of flavors available with a summary description
        (Name, Disk, CPU, RAM) and number of instances start-able with
        current Cloud state, maximum instances start-able when Cloud is
        empty
        :return: dict()
        """
        return {
            'full.90%': {
                'name': 'full.90%',
                'disk': 10,
                'ram': 1024,
                'cpu': 1,
                'free': 10,
                'max': 100,
            },
            'full.80%': {
                'name': 'full.80%',
                'disk': 20,
                'ram': 2048,
                'cpu': 2,
                'free': 20,
                'max': 100,
            },
            'full.70%': {
                'name': 'full.70%',
                'disk': 30,
                'ram': 3072,
                'cpu': 3,
                'free': 30,
                'max': 100,
            },
            'full.60%': {
                'name': 'full.60%',
                'disk': 30,
                'ram': 3072,
                'cpu': 3,
                'free': 40,
                'max': 100,
            },
            'full.50%': {
                'name': 'full.50%',
                'disk': 30,
                'ram': 3072,
                'cpu': 3,
                'free': 50,
                'max': 100,
            },
            'full.10%': {
                'name': 'full.10%',
                'disk': 30,
                'ram': 3072,
                'cpu': 3,
                'free': 90,
                'max': 100,
            }
        }

    @staticmethod
    def projects():
        """
        Return a list of project w/ any useful information
        :return: dict()
        """
        return {
            '1' : {
                'id': '1',
                'name': 'Project 1'
            },
            '2': {
                'id': '2',
                'name': 'Project 2'
            }
        }

    @staticmethod
    def lease_instance(request, instance_id):
        """
        If instance_id is owned by user_id, then update lease information, if not, raise
        PermissionDenied exception
        :param instance_id: id of instance
        :param request: Web request
        :return: void
        """
        data_instances = TestConnection.instances(None)
        # To avoid int vs string comparaison, we force user_id and request.user.id to be
        # a string
        if str(data_instances[instance_id]['user_id']) != str(request.user.id):
            raise PermissionDenied(request.user.id, instance_id)
        InstancesAccess.save({
            instance_id: data_instances[instance_id]
        })
