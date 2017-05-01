"""
This module manage interaction between application and
OpenStack cloud infrastructure
"""
#  -*- coding: utf-8 -*-

import math
from django.core.cache import cache
from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as nvclient
from openstack_lease_it.settings import GLOBAL_CONFIG
from lease_it.datastore import InstancesAccess

# Define nova client version as a constant
NOVA_VERSION = 2

# Default cache timeout for flavor (in sec)
FLAVOR_CACHE_TIMEOUT = 86400


class OpenstackConnection(object):  # pylint: disable=too-few-public-methods
    """
    This class manage interface between OpenStack Cloud infrastructure and
    views.
    """
    def __init__(self):
        """
        During class initialization, we create a connection to
        OpenStack Cloud
        """
        super(OpenstackConnection, self).__init__()
        # We need to be admin to have access to hypervisor list
        credentials = dict()
        credentials['username'] = GLOBAL_CONFIG['OS_USERNAME']
        credentials['password'] = GLOBAL_CONFIG['OS_PASSWORD']
        credentials['auth_url'] = GLOBAL_CONFIG['OS_AUTH_URL']
        credentials['project_name'] = GLOBAL_CONFIG['OS_PROJECT_NAME']
        credentials['project_domain_name'] = GLOBAL_CONFIG['OS_PROJECT_DOMAIN_NAME']
        credentials['user_domain_name'] = GLOBAL_CONFIG['OS_USER_DOMAIN_NAME']

        try:
            auth = v3.Password(**credentials)
            self.session = session.Session(auth=auth,
                                           verify=GLOBAL_CONFIG['OS_CACERT'])
        except:  # pylint: disable=bare-except
            pass

    def _instances(self, request):
        """
        List of instances actually launched
        :return: dict()
        """
        # user_token = v3.Token(token=request.user.token.id,
        #                 auth_url=GLOBAL_CONFIG['OS_AUTH_URL'],
        #                 project_name='admin',  # TODO: Should be compute
        #                 project_domain_name='default')  # TODO: Should be compute
        # user_session = session.Session(auth=user_token,
        #                                verify=GLOBAL_CONFIG['OS_CACERT'])
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        data_instances = nova.servers.list(search_opts={'all_tenants': 'true'})
        return data_instances

    def _hypervisors(self):
        """
        List of hypervisors and their details
        :return: dict()
        """
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        hypervisors = nova.hypervisors.list()
        return hypervisors

    def _flavors(self):
        """
        List of flavors and their details
        """
        response = dict()
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        flavors = nova.flavors.list()
        for flavor in flavors:
            response[flavor.name] = {
                'name': flavor.name,
                'disk': int(flavor.disk),
                'ram': int(flavor.ram),
                'cpu': int(flavor.vcpus)
            }
        return response

    def flavors(self):
        """
        Return a list of flavor and a detail about
        * Their properties (CPU / Disk / RAM)
        * The actual Cloud state (number of VM we can start, maximum
        VM we can start if empty)
        :return: dict()
        """
        # We retrieve information from memcached
        flavors = cache.get('flavors')
        if not flavors:
            # If cache is empty we retrieve information from Openstack
            # and we set it in cached
            flavors = self._flavors()
            cache.set('flavors', flavors, FLAVOR_CACHE_TIMEOUT)

        # Retrieve hypervisor status to populate response
        hypervisors = self._hypervisors()

        # For each flavor, we look @ each hypervisor how many of
        # it can be launch @ the current state and the maximum value
        # based on flavor
        # * disk
        # * CPU
        # * RAM
        for flavor in flavors:
            free_flavor = 0
            max_flavor = 0
            for hypervisor in hypervisors:
                # If hypervisor is disable or down we don't care of it
                if hypervisor.status == "enabled" and\
                                hypervisor.state == "up":
                    # We round down the number of flavor
                    free_cpu = math.floor((hypervisor.vcpus - hypervisor.vcpus_used) /
                                          flavors[flavor]['cpu'])
                    max_cpu = math.floor(hypervisor.vcpus / flavors[flavor]['cpu'])
                    free_ram = math.floor(hypervisor.free_ram_mb / flavors[flavor]['ram'])
                    max_ram = math.floor(hypervisor.memory_mb / flavors[flavor]['ram'])
                    free_disk = math.floor(hypervisor.free_disk_gb / flavors[flavor]['disk'])
                    max_disk = math.floor(hypervisor.local_gb / flavors[flavor]['disk'])

                    # We keep the lowest value of ram / cpu / disk as it s
                    # the weak link of the hypervisor
                    if min(free_cpu, free_ram, free_disk) > 0:
                        free_flavor += min(free_cpu, free_ram, free_disk)
                    if min(max_cpu, max_ram, max_disk) > 0:
                        max_flavor += min(max_cpu, max_ram, max_disk)
            flavors[flavor]['free'] = free_flavor
            flavors[flavor]['max'] = max_flavor
        return flavors

    def instances(self, request):
        response = dict()
        data_instances = self._instances(request)
        for instance in data_instances:
            if instance.user_id == request.user.id:
                response[instance.id] = {
                    'user_id': instance.user_id,
                    'project_id': instance.tenant_id,
                    'id': instance.id,
                    'name': instance.name,
                    'created_at': instance.created
                }
        print response
        return InstancesAccess.show(response)

    def users(self):
        return dict()

    def projects(self):
        return dict()
