#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as ksclient
from novaclient import client as nvclient


class OpenstackConnection(object):
    """

    """
    def __init__(self,
                 config):
        super(OpenstackConnection, self).__init__()
        self.global_config = config
        self.username = self.global_config['OS_USERNAME']
        self.password = self.global_config['OS_PASSWORD']
        self.tenant_name = self.global_config['OS_TENANT_NAME']
        self.project_name = self.global_config['OS_PROJECT_NAME']
        self.auth_url = self.global_config['OS_AUTH_URL']
        self.identity_api_version = self.global_config['OS_IDENTITY_API_VERSION']
        self.cacert = self.global_config['OS_CACERT']
        self.user_domain_name = self.global_config['OS_USER_DOMAIN_NAME']
        self.project_domain_name = self.global_config['OS_PROJECT_DOMAIN_NAME']

        creds = {}
        creds['username'] = self.username
        creds['password'] = self.password
        creds['auth_url'] = self.auth_url
        creds['project_name'] = self.project_name
        creds['project_domain_name'] = self.project_domain_name
        creds['user_domain_name'] = self.user_domain_name

        try:
            self.auth = v3.Password(**creds)
            self.sess = session.Session(auth=self.auth,verify=self.cacert)
        except:
            pass


    def nova_get_instances(self):
        VERSION = '2'
        nova = nvclient.Client(VERSION, session=self.sess)
        instances = nova.servers.list(search_opts={'all_tenants': 'true'})

        # for each in instances:
        #     print each._info
        #     print "--------------------------"

        return instances

    def nova_get_hypervisors(self):
        VERSION = '2'
        nova = nvclient.Client(VERSION, session=self.sess)
        hypervisors = nova.hypervisors.list()

        return hypervisors

    def nova_get_flavors(self):
        VERSION = '2'
        nova = nvclient.Client(VERSION, session=self.sess)
        flavors = nova.flavors.list()

        return flavors

    def keystone_get_user(self,
                          name=None,
                          uid=None):
        """

        :param name:
        :param uid:
        :return:
        """
        keystone = ksclient.Client(session=self.sess)
        # users = keystone.users.list()
        token = keystone.tokens
        print type(token)
        return token


