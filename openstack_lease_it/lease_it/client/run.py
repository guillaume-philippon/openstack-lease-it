#  -*- coding: utf-8 -*-
"""
instance-spy should be put on a crontab to check running instance, notify user if lease is close
to expire and destroy instance when lease is over
"""
import os
import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

os.environ['DJANGO_SETTINGS_MODULE'] = "openstack_lease_it.settings"

from lease_it import backend  # pylint: disable=wrong-import-position
from openstack_lease_it.settings import GLOBAL_CONFIG  # pylint: disable=wrong-import-position

# We load backend specify by configuration file
BACKEND_PLUGIN = getattr(backend, "{0}Connection".format(GLOBAL_CONFIG['BACKEND_PLUGIN']))
BACKEND = BACKEND_PLUGIN()  # pylint: disable=not-callable

# Default file content
MAIL_CONTENT_DELETE="""
Hi,

Some of your Virtual Machine on Cloud@VD have been removed due to expire lease time :
{0}
"""

MAIL_CONTENT_NOTIFY="""
Hi,

Some of your Virtual Machine on Cloud@VD are close to expire, please update the lease date on 
https://lease-it.lal.in2p3.fr :
{0}
"""


def instance_spy():
    """
    Function used to run the script
    :return: void
    """
    instances = BACKEND.spy_instances()
    users = BACKEND.users()
    for type in "delete", "notify":
        users_to_notify = defaultdict(str)
        for instance in instances[type]:
            try:
                users_to_notify[instance['user_id']] += "    - {name} started {created_at} and last " \
                                                        "lease {lease_end}\n".format(**instance)
                # print(users[instance['user_id']]['email'])  # pylint: disable=superfluous-parens
            except KeyError:
                pass
        for user_id, user_to_notify in users_to_notify.iteritems():
            format_mail(user_to_notify, type)


def format_mail(user, type):
    if type == "delete":
        print MAIL_CONTENT_DELETE.format(user)
    elif type == "notify":
        print MAIL_CONTENT_NOTIFY.format(user)


def admin_cli():
    """
    Admin Command Line Interface
    :return: void
    """
    return True
