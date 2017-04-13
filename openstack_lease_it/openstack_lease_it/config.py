"""
This module manage configuration file.
* /etc/openstack-lease-it/config.ini
* $HOME/.lease-it.ini
"""
import ConfigParser
import os

# List possible configuration file, last item has highest priority
CONFIG_FILES = (
    '/etc/openstack-lease-it/config.ini',
    os.path.expanduser('~') + '/.lease-it.ini',
)


def read_configuration_file():
    # Define default configuration, *NOT* all value have a default
    global_configuration = {
        # Django parameters
        'DEBUG': False,

        # OpenStack parameters
        'OS_USERNAME': 'admin',
        'OS_TENANT_NAME': 'admin',
        'OS_PROJECT_NAME': 'admin',
        'OS_IDENTITY_API_VERSION': '3',
        'OS_USER_DOMAIN_NAME': 'default',
        'OS_PROJECT_DOMAIN_NAME': 'default',
    }
    config = ConfigParser.RawConfigParser()

    for file in CONFIG_FILES:
        config.read(file)

        try:
            global_configuration['SECRET_KEY'] = config.get('django','secret_key')
        except:
            pass
        try:
            global_configuration['DEBUG'] = config.getboolean('django', 'debug')
        except:
            pass

        try:
            global_configuration['OS_USERNAME'] = config.get('openstack', 'OS_USERNAME')
        except:
            pass
        try:
            global_configuration['OS_PASSWORD'] = config.get('openstack', 'OS_PASSWORD')
        except:
            pass
        try:
            global_configuration['OS_TENANT_NAME'] = config.get('openstack', 'OS_TENANT_NAME')
        except:
            pass
        try:
          global_configuration['OS_PROJECT_NAME'] = config.get('openstack', 'OS_PROJECT_NAME')
        except:
            pass
        try:
            global_configuration['OS_AUTH_URL'] = config.get('openstack', 'OS_AUTH_URL')
        except:
            pass
        try:
            global_configuration['OS_IDENTITY_API_VERSION'] = config.get('openstack', 'OS_IDENTITY_API_VERSION')
        except:
            pass
        try:
            global_configuration['OS_CACERT'] = config.get('openstack', 'OS_CACERT')
        except:
            pass
        try:
            global_configuration['OS_USER_DOMAIN_NAME'] = config.get('openstack', 'OS_USER_DOMAIN_NAME')
        except:
            pass
        try:
            global_configuration['OS_PROJECT_DOMAIN_NAME'] = config.get('openstack', 'OS_PROJECT_DOMAIN_NAME')
        except:
            pass

    return global_configuration
