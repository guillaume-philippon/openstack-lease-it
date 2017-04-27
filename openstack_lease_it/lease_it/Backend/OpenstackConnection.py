"""
This module manage interaction between application and
OpenStack cloud infrastructure
"""
#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import math
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as ksclient
from novaclient import client as nvclient
from openstack_lease_it.settings import GLOBAL_CONFIG

# Define nova client version as a constant
NOVA_VERSION = 2


class OpenstackConnection(object): # pylint: disable=too-many-instance-attributes
    """
    OpenstackConnection class
    """
    def __init__(self):
        """
        During class initialization, we create a connection to
        OpenStack Cloud
        """
        super(OpenstackConnection, self).__init__()
        # We need to be admin to have access to hypervisor list
        self.username = GLOBAL_CONFIG['OS_USERNAME']
        self.password = GLOBAL_CONFIG['OS_PASSWORD']
        self.tenant_name = GLOBAL_CONFIG['OS_TENANT_NAME']
        self.project_name = GLOBAL_CONFIG['OS_PROJECT_NAME']
        self.auth_url = GLOBAL_CONFIG['OS_AUTH_URL']
        self.identity_api_version = GLOBAL_CONFIG['OS_IDENTITY_API_VERSION']
        self.ca_cert = GLOBAL_CONFIG['OS_CACERT']
        self.user_domain_name = GLOBAL_CONFIG['OS_USER_DOMAIN_NAME']
        self.project_domain_name = GLOBAL_CONFIG['OS_PROJECT_DOMAIN_NAME']

        credentials = dict()
        credentials['username'] = self.username
        credentials['password'] = self.password
        credentials['auth_url'] = self.auth_url
        credentials['project_name'] = self.project_name
        credentials['project_domain_name'] = self.project_domain_name
        credentials['user_domain_name'] = self.user_domain_name

        try:
            self.auth = v3.Password(**credentials)
            self.session = session.Session(auth=self.auth,
                                           verify=self.ca_cert)
        except:  # pylint: disable=bare-except
            pass

    def instances(self):
        """
        List of instances actually launched
        :return: dict()
        """
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        instances = nova.servers.list(search_opts={'all_tenants': 'true'})
        return instances

    def hypervisors(self):
        """
        List of hypervisors and their details
        :return: dict()
        """
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        hypervisors = nova.hypervisors.list()
        return hypervisors

    def flavors(self):
        """
        List of flavors and their details
        """
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        flavors = nova.flavors.list()
        return flavors

    def keystone_get_user(self):
        """
        List of users and their details
        This function need access to OpenStack admin network
        :return: token
        """
        keystone = ksclient.Client(session=self.session)
        token = keystone.tokens
        return token

    def usage(self):
        """
        Return a list of flavor and a detail about
        * Their properties (CPU / Disk / RAM)
        * The actual Cloud state (number of VM we can start, maximum
        VM we can start if empty)
        :return: dict()
        """
        # Create a empty dictionnary as default response
        response = dict()

        # Retrieve flavor list from OpenStack and populate response
        # with useful information
        flavors = self.flavors()
        # Retrieve hypervisor status to populate response
        hypervisors = self.hypervisors()
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
                    free_cpu = math.floor((hypervisor.vcpus - hypervisor.vcpus_used) / flavor.vcpus)
                    max_cpu = math.floor(hypervisor.vcpus / flavor.vcpus)
                    free_ram = math.floor(hypervisor.free_ram_mb / flavor.ram)
                    max_ram = math.floor(hypervisor.memory_mb / flavor.ram)
                    free_disk = math.floor(hypervisor.free_disk_gb / flavor.disk)
                    max_disk = math.floor(hypervisor.local_gb / flavor.disk)

                    # We keep the lowest value of ram / cpu / disk as it s
                    # the weak link of the hypervisor
                    if min(free_cpu, free_ram, free_disk) > 0:
                        free_flavor += min(free_cpu, free_ram, free_disk)
                    if min(max_cpu, max_ram, max_disk) > 0:
                        max_flavor += min(max_cpu, max_ram, max_disk)
            response[flavor.name] = {
                'name': flavor.name,
                'disk': flavor.disk,
                'ram': flavor.ram,
                'cpu': flavor.vcpus,
                'free': free_flavor,
                'max': max_flavor
            }
        return response
