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
Hi {0},

Some of your Virtual Machine on Cloud@VD have been removed due to expire lease time :
{1}
"""

MAIL_CONTENT_NOTIFY="""
Hi {0},

Some of your Virtual Machine on Cloud@VD are close to expire, please update the lease date on 
https://lease-it.lal.in2p3.fr :
{1}
"""


def instance_spy():
    """
    Function used to run the script
    :return: void
    """
    instances = BACKEND.spy_instances()
    users = BACKEND.users()
    for notification_type in "delete", "notify":
        users_to_notify = defaultdict(str)
        for instance in instances[notification_type]:
            # TODO: I really don't like it
            users_to_notify[instance['user_id']] += "    - {name} started {created_at} and last " \
                                                    "lease {lease_end}\n".format(**instance)
        for user_id, user_instances in users_to_notify.iteritems():
            try:
                format_mail(users[user_id], user_instances, notification_type)
            except KeyError:
                print("No user information found for user_id {0} and instance {1}".format(
                    user_id,
                    user_instances
                    ))


def format_mail(user, instances, notification_type):
    # TODO: Should be a dedicated Class
    subject = "Cloud@VD virtual machine notification"
    if notification_type == "delete":
        try:
            content = MAIL_CONTENT_DELETE.format(user['name'], instances)
        except KeyError:
            content = MAIL_CONTENT_DELETE.format('', instances)
    elif notification_type == "notify":
        try:
            content = MAIL_CONTENT_NOTIFY.format(user['name'], instances)
        except KeyError:
            content = MAIL_CONTENT_DELETE.format('', instances)
    mail = MIMEText(content)
    mail['Subject'] = subject
    mail['From'] = GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']
    mail['To'] = user['email']
    # notification = smtplib.SMTP_SSL(GLOBAL_CONFIG['NOTIFICATION_SMTP'])
    # notification.login(GLOBAL_CONFIG['NOTIFICATION_USERNAME'],
    #                    GLOBAL_CONFIG['NOTIFICATION_PASSWORD'])
    # notification.sendmail(GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER'],
    #                       [GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']],
    #                       mail.as_string())
    # notification.quit()
    print mail.as_string()


def admin_cli():
    """
    Admin Command Line Interface
    :return: void
    """
    return True
