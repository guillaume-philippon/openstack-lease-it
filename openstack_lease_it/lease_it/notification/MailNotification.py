"""
Mail notification system
"""

import smtplib
import ast
import re
from email.mime.text import MIMEText
from openstack_lease_it.settings import GLOBAL_CONFIG, EMAIL_REGEXP
from openstack_lease_it.settings import LOGGER

# Default file content
MAIL_CONTENT = {'delete': """
Hi {0},

Some of your Virtual Machine on Cloud will been removed due to expire lease time, you can update
the lease on {1} :
{2}

--
OpenStack team
""",
                'notify': """
Hi {0},

Some of your Virtual Machine on Cloud are close to expire, please update the lease date on 
{1} :
{2}
"""}


class MailNotification(object):  # pylint: disable=too-few-public-methods
    """
    A class to abstract e-mail notification
    """
    def __init__(self, users):
        """
        Not yet implemented
        """
        self.users = users
        self.smtp = smtplib.SMTP_SSL(GLOBAL_CONFIG['NOTIFICATION_SMTP'])
        self.smtp.login(GLOBAL_CONFIG['NOTIFICATION_USERNAME'],
                        GLOBAL_CONFIG['NOTIFICATION_PASSWORD'])

    @staticmethod
    def format_user_instances(user):
        """
        Create a string w/ the list of instance formatted to be mailed
        :param user: user we currently notify
        :return: string
        """
        text = ""
        for instance in user:
            text += "  - {name} started {created_at} and expire {lease_end} \n".format(**instance)
        return text

    def format_mail(self, user, notification_type, instances):
        """
        Format the mail content
        :param user: user we currently notify
        :param notification_type: notification type (delete or notify)
        :param instances: list of instance for the user
        :return: string
        """
        try:
            user_name = self.users[user]['name']
        except KeyError:
            user_name = 'Unknown User'
            LOGGER.info("User %s as not be found", user)
        core_text = MAIL_CONTENT[notification_type]
        instances_text = self.format_user_instances(instances)
        return core_text.format(user_name,
                                GLOBAL_CONFIG['NOTIFICATION_LINK'],
                                instances_text)

    def send(self, notifications):
        """
        The all notifications give in parameter, each notifications type (delete or notify) are
        a dictionnary of users with a list of instance to notify per user
        :param notifications: dict of users and instances
        :return: void
        """
        for notification in notifications:
            for user in notifications[notification]:
                mail_text = self.format_mail(user, notification, notifications[notification][user])
                mail = MIMEText(mail_text)
                mail['Subject'] = GLOBAL_CONFIG['NOTIFICATION_SUBJECT']
                mail['From'] = GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']
                try:
                    email = self.users[user]['email']
                    if not re.match(EMAIL_REGEXP, email) and \
                                    GLOBAL_CONFIG['NOTIFICATION_DOMAIN'] != "":
                        LOGGER.info("email %s not match a email format (name@domain.com). "
                                    "Add @%s",
                                    email, GLOBAL_CONFIG['NOTIFICATION_DOMAIN'])
                        email = "{0}@{1}".format(email, GLOBAL_CONFIG['NOTIFICATION_DOMAIN'])
                    mail['To'] = email
                    if ast.literal_eval(GLOBAL_CONFIG['NOTIFICATION_DEBUG']):
                        LOGGER.info("Only notify administrator instead of %s", email)
                        recipient = [GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']]
                    else:
                        recipient = [GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER'],
                                     email]
                except KeyError:
                    LOGGER.info("email field of %s as not be found", user)
                    mail['To'] = GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']
                    recipient = [GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']]
                LOGGER.info("Notification %s to %s", notification, ''.join(recipient))
                self.smtp.sendmail(GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER'],
                                   recipient,
                                   mail.as_string())
