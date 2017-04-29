"""
TestConnection is a module of Fake backend used to help developpement
of API
"""
# -*- coding: utf-8 -*-


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
        return {
            '1': {
                'id': '1',
                'firstname': 'John',
                'lastname': 'Smith',
                'mail': 'john.smith@example.com'
            },
            '2': {
                'id': '2',
                'firstname': 'Jane',
                'lastname': 'Doe',
                'mail': 'jane.doe@fake.com'
            },
        }

    @staticmethod
    def instances():
        """
        Return a list of fake value for some instances. Each instances
        is must contain owner id, project id, instance id, name of the
        instance, starting date of instance, last time a lease as been put,
        the leasing duration
        :return: dict()
        """
        return {
            '1': {
                'user_id': '1',
                'project_id': '1',
                'id': '1',
                'name': 'user1_project1_expire',
                'created_at': '01/20/2014',
                'last_lease_at': '01/10/2016',
                'lease_time': 3
            },
            '2': {
                'user_id': '1',
                'project_id': '1',
                'id': '2',
                'name': 'user1_project1_expire',
                'created_at': '01/20/2014',
                'last_lease_at': '01/10/2016',
                'lease_time': 3
            },
            '3': {
                'user_id': '1',
                'project_id': '1',
                'id': '3',
                'name': 'user1_project1_close_to',
                'created_at': '01/20/2014',
                'last_lease_at': '01/01/2017',
                'lease_time': 3
            },
            '4': {
                'user_id': '1',
                'project_id': '1',
                'id': '4',
                'name': 'user1_project1_renew',
                'created_at': '01/04/2014',
                'last_lease_at': '01/10/2016',
                'lease_time': 3
            },
        }

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
