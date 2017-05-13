#  -*- coding: utf-8 -*-
"""
instance-spy should be put on a crontab to check running instance, notify user if lease is close
to expire and destroy instance when lease is over
"""
import os

os.environ['DJANGO_SETTINGS_MODULE'] = "openstack_lease_it.settings"

from lease_it import backend  # pylint: disable=wrong-import-position
from openstack_lease_it.settings import GLOBAL_CONFIG  # pylint: disable=wrong-import-position

# We load backend specify by configuration file
BACKEND_PLUGIN = getattr(backend, "{0}Connection".format(GLOBAL_CONFIG['BACKEND_PLUGIN']))
BACKEND = BACKEND_PLUGIN()  # pylint: disable=not-callable


def instance_spy():
    """
    Function used to run the script
    :return: void
    """
    instances = BACKEND.spy_instances()
    users = BACKEND.users()
    for instance in instances['delete']:
        print(users[instance['user_id']]['email'])  # pylint: disable=superfluous-parens


def admin_cli():
    """
    Admin Command Line Interface
    :return: void
    """
    return True
