"""
This module manage configuration file.

    - /etc/openstack-lease-it/config.ini
    - $HOME/.lease-it.ini
"""
import ConfigParser
import os

BASE_CONFIG_DIR = '/etc/openstack-lease-it'
"""
Configuration directory
"""

CONFIG_FILES = (
    BASE_CONFIG_DIR + '/config.ini',
    os.path.expanduser('~') + '/.lease-it.ini',
)
"""
Configuration files, the last one have highest priority
"""

GLOBAL_CONFIG = {
    # Django parameters
    'DJANGO_DEBUG': 'False',
    'DJANGO_LOGDIR': '/var/log/openstack-lease-it/',
    'DJANGO_LOGLEVEL': 'INFO',

    # OpenStack parameters
    'OS_USERNAME': 'admin',
    'OS_TENANT_NAME': 'admin',
    'OS_PROJECT_NAME': 'admin',
    'OS_IDENTITY_API_VERSION': '3',
    'OS_USER_DOMAIN_NAME': 'default',
    'OS_PROJECT_DOMAIN_NAME': 'default',

    # memcached parameter
    'MEMCACHED_HOST': '127.0.0.1',
    'MEMCACHED_PORT': '11211',

    # plugins parameter
    'BACKEND_PLUGIN': 'Openstack',

    # notification parameter
    'NOTIFICATION_DEBUG': 'False',
    'NOTIFICATION_DOMAIN': '',
    'NOTIFICATION_DELETE_CONTENT': BASE_CONFIG_DIR + '/delete-notification.txt',
    'NOTIFICATION_LEASE_CONTENT': BASE_CONFIG_DIR + '/lease-notification.txt'
}
"""
global variable used to share configuration across modules
"""

DJANGO_OPTIONS = {
    'DJANGO_SECRET_KEY': 'secret_key',
    'DJANGO_DEBUG': 'debug',
    'DJANGO_LOGDIR': 'log_dir',
    'DJANGO_LOGLEVEL': 'log_level'
}
"""
options for section [django]
"""

PLUGINS_OPTIONS = {
    'BACKEND_PLUGIN': 'backend'
}
"""
options for section [plugins]
"""

OPENSTACK_OPTIONS = {
    'OS_USERNAME': 'OS_USERNAME',
    'OS_PASSWORD': 'OS_PASSWORD',
    'OS_TENANT_NAME': 'OS_TENANT_NAME',
    'OS_PROJECT_NAME': 'OS_PROJECT_NAME',
    'OS_AUTH_URL': 'OS_AUTH_URL',
    'OS_CACERT': 'OS_CACERT',
    'OS_IDENTITY_API_VERSION': 'OS_IDENTITY_API_VERSION',
    'OS_PROJECT_DOMAIN_NAME': 'OS_PROJECT_DOMAIN_NAME',
    'OS_USER_DOMAIN_NAME': 'OS_USER_DOMAIN_NAME'
}
"""
options for section [openstack]
"""

# Default options for section [memcached]
MEMCACHED_OPTIONS = {
    'MEMCACHED_HOST': 'host',
    'MEMCACHED_PORT': 'port'
}

# Default options for section [notification]
NOTIFICATION_OPTIONS = {
    'NOTIFICATION_SSL': 'ssl',
    'NOTIFICATION_SMTP': 'smtp',
    'NOTIFICATION_USERNAME': 'username',
    'NOTIFICATION_PASSWORD': 'password',
    'NOTIFICATION_EMAIL_HEADER': 'email_header',
    'NOTIFICATION_SUBJECT': 'subject',
    'NOTIFICATION_LINK': 'link',
    'NOTIFICATION_DEBUG': 'debug',
    'NOTIFICATION_DOMAIN': 'default_domain',
    'NOTIFICATION_DELETE_CONTENT': 'delete_content',
    'NOTIFICATION_LEASE_CONTENT': 'lease_content'
}

SECTIONS = {
    'django': DJANGO_OPTIONS,
    'openstack': OPENSTACK_OPTIONS,
    'memcached': MEMCACHED_OPTIONS,
    'plugins': PLUGINS_OPTIONS,
    'notification': NOTIFICATION_OPTIONS
}
"""
List of all section that will be compute and options associated w/ those sections
"""

def load_config_option(config, section):
    """
    This function overwrite the current global_config[name] value
    with option

    :param config: Configuration file we read
    :param section: The section of configuration file we compute
    :return: void
    """
    options = SECTIONS[section]
    for option in options:
        try:
            GLOBAL_CONFIG[option] = config.get(section,
                                               options[option])
        except ConfigParser.NoSectionError:
            pass
        except ConfigParser.NoOptionError:
            pass


def load_config():
    """
    Define default configuration, *NOT* all value have a default

    :return: void
    """
    config = ConfigParser.RawConfigParser()

    for config_file in CONFIG_FILES:
        config.read(config_file)
        for section in SECTIONS:
            load_config_option(config, section)
