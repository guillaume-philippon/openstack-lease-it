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
the lease on {1}:
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
        # self.smtp = smtplib.SMTP_SSL(GLOBAL_CONFIG['NOTIFICATION_SMTP'])
        # self.smtp.login(GLOBAL_CONFIG['NOTIFICATION_USERNAME'],
        #                 GLOBAL_CONFIG['NOTIFICATION_PASSWORD'])

    @staticmethod
    def format_user_instances(user):
        text = ""
        for instance in user:
            text += "  - {name} started {created_at} and expire {lease_end} \n".format(**instance)
        return text

    def send(self, notifications):
        for notification in notifications:
            for user in notifications[notification]:
                instance_text = self.format_user_instances(notifications[notification][user])
                try:
                    user_name = self.users[user]['name']
                except KeyError:
                    user_name = "Unknowned User"
                core_text = MAIL_CONTENT[notification]
                print core_text.format(user_name,
                                           GLOBAL_CONFIG['NOTIFICATION_LINK'],
                                           instance_text)


        # self.smtp.sendmail(GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER'],
        #                       [GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']],
        #                       mail.as_string())
        # notification.quit()


# def format_mail(user, instances, notification_type):
#     # TODO: Should be a dedicated Class
#     subject = "Cloud@VD virtual machine notification"
#     if notification_type == "delete":
#         try:
#             content = MAIL_CONTENT_DELETE.format(user['name'], instances)
#         except KeyError:
#             content = MAIL_CONTENT_DELETE.format('', instances)
#     elif notification_type == "notify":
#         try:
#             content = MAIL_CONTENT_NOTIFY.format(user['name'], instances)
#         except KeyError:
#             content = MAIL_CONTENT_DELETE.format('', instances)
#     mail = MIMEText(content)
#     mail['Subject'] = subject
#     mail['From'] = GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']
#     mail['To'] = user['email']
    # notification = smtplib.SMTP_SSL(GLOBAL_CONFIG['NOTIFICATION_SMTP'])
    # notification.login(GLOBAL_CONFIG['NOTIFICATION_USERNAME'],
    #                    GLOBAL_CONFIG['NOTIFICATION_PASSWORD'])
    # notification.sendmail(GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER'],
    #                       [GLOBAL_CONFIG['NOTIFICATION_EMAIL_HEADER']],
    #                       mail.as_string())
    # notification.quit()
    # print mail.as_string()

