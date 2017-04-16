#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as ksclient
from novaclient import client as nvclient
from openstack_lease_it.settings import GLOBAL_CONFIG
import math

# Define nova client version as a constant
NOVA_VERSION = 2


class OpenstackConnection(object):
    def __init__(self):
        super(OpenstackConnection, self).__init__()
        # We need to be admin to have access to hypervisor list
        self.username = GLOBAL_CONFIG['OS_USERNAME']
        self.password = GLOBAL_CONFIG['OS_PASSWORD']
        self.tenant_name = GLOBAL_CONFIG['OS_TENANT_NAME']
        self.project_name = GLOBAL_CONFIG['OS_PROJECT_NAME']
        self.auth_url = GLOBAL_CONFIG['OS_AUTH_URL']
        self.identity_api_version = GLOBAL_CONFIG['OS_IDENTITY_API_VERSION']
        self.cacert = GLOBAL_CONFIG['OS_CACERT']
        self.user_domain_name = GLOBAL_CONFIG['OS_USER_DOMAIN_NAME']
        self.project_domain_name = GLOBAL_CONFIG['OS_PROJECT_DOMAIN_NAME']

        creds = dict()
        creds['username'] = self.username
        creds['password'] = self.password
        creds['auth_url'] = self.auth_url
        creds['project_name'] = self.project_name
        creds['project_domain_name'] = self.project_domain_name
        creds['user_domain_name'] = self.user_domain_name

        try:
            self.auth = v3.Password(**creds)
            self.session = session.Session(auth=self.auth,
                                           verify=self.cacert)
        except:
            pass

    def instances(self, request):
        response = dict()
        test = v3.Token(token=request.user.token.id,
                        auth_url=self.auth_url,
                        project_name='admin',  # TODO: Should be compute
                        project_domain_name='default')  # TODO: Should be compute
        test_session = session.Session(auth=test, verify=self.cacert)
        print test_session.auth.__dict__
        print self.session.auth.__dict__
        keystone = ksclient.Client(session=test_session)
        nova = nvclient.Client(NOVA_VERSION, session=test_session)
        # nova = nvclient.Client(NOVA_VERSION, session=self.session)
        instances = nova.servers.list(search_opts={'all_tenants': 'true'})
        for instance in instances:
            response[instance.id] = {
                'status': instance.status,
                'created': instance.created,
                'name': instance.name,
                'project_id': instance.tenant_id,
                'user': instance.user_id
            }
        return response

    def hypervisors(self):
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        hypervisors = nova.hypervisors.list()
        return hypervisors

    def flavors(self):
        nova = nvclient.Client(NOVA_VERSION, session=self.session)
        flavors = nova.flavors.list()
        return flavors

    def keystone_get_user(self):
        keystone = ksclient.Client(session=self.session)
        token = keystone.tokens
        print(type(token))
        return token

    def usage(self):
        # Create a empty dictionnary as default response
        response = dict()

        # Retrieve flavor list from OpenStack and populate response with useful information
        flavors = self.flavors()
        # Retrieve hypervisor status to populate response
        hypervisors = self.hypervisors()
        # For each flavor, we look @ each hypervisor how many of it can be launch @ the current state
        # and the maximum value based on flavor
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

                    # We keep the lowest value of ram / cpu / disk as it s the weak link of the hypervisor
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
