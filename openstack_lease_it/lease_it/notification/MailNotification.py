"""
Mail notification system
"""

import smtplib
from email.mime.text import MIMEText
from openstack_lease_it.settings import GLOBAL_CONFIG

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
        text = ""
        for instance in user:
            text += "  - {name} started {created_at} and expire {lease_end} \n".format(**instance)
        return text

    def format_mail(self, user, notification_type, instances):
        try:
            user_name = self.users[user]['name']
        except KeyError:
            user_name = 'Unknown User'
        core_text = MAIL_CONTENT[notification_type]
        instances_text = self.format_user_instances(instances)
        return core_text.format(user_name,
                                GLOBAL_CONFIG['NOTIFICATION_LINK'],
                                instances_text)

    def send(self, notifications):
        for notification in notifications:
            for user in notifications[notification]:
                mail_text = self.format_mail(user, notification, notifications[notification][user])
                mail = MIMEText(mail_text)
                mail['Subject'] = GLOBAL_CONFIG['NOTIFICATION_SUBJECT']
                mail['From'] = GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']
                try:
                    mail['To'] = self.users[user]['email']
                except KeyError:
                    mail['To'] = GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']
                self.smtp.sendmail(GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER'],
                                   [GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']],
                                   mail.as_string())
