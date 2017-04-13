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


OPTIONS = {
    # [django] section
    'SECRET_KEY': {
        'section':'django',
        'option': 'secret_key'
    },
    'DEBUG': {
        'section':'django',
        'option': 'debug'
    },

    # [openstack] section
    'OS_USERNAME': {
        'section':'openstack',
        'option': 'OS_USERNAME'
    },
    'OS_PASSWORD': {
        'section':'openstack',
        'option': 'OS_PASSWORD'
    },
    'OS_TENANT_NAME': {
        'section':'openstack',
        'option': 'OS_TENANT_NAME'
    },
    'OS_PROJECT_NAME': {
        'section':'openstack',
        'option': 'OS_PROJECT_NAME'
    },
    'OS_AUTH_URL': {
        'section':'openstack',
        'option': 'OS_AUTH_URL'
    },
    'OS_CACERT': {
        'section':'openstack',
        'option': 'OS_CACERT'
    },
    'OS_IDENTITY_API_VERSION': {
        'section':'openstack',
        'option': 'OS_IDENTITY_API_VERSION'
    },
    'OS_PROJECT_DOMAIN_NAME': {
        'section':'openstack',
        'option': 'OS_PROJECT_DOMAIN_NAME'
    },
    'OS_USER_DOMAIN_NAME': {
        'section':'openstack',
        'option': 'OS_USER_DOMAIN_NAME'
    },

    # [memcached] section
    'MEMCACHED_HOST': {
        'section':'memcached',
        'option': 'host'
    },
    'MEMCACHED_PORT': {
        'section':'memcached',
        'option': 'port'
    }
}


def load_config_option(global_config, config, name, option):
    try:
        global_config[name] = config.get(option['section'],
                                         option['option'])
    except ConfigParser.NoSectionError:
        pass
    except ConfigParser.NoOptionError:
        pass


def load_config():
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

        # memcached parameter
        'MEMCACHED_HOST': '127.0.0.1',  #nosonar
        'MEMCACHED_PORT': '11211'
    }
    config = ConfigParser.RawConfigParser()

    for config_file in CONFIG_FILES:
        config.read(config_file)
        for option in OPTIONS:
            load_config_option(global_configuration,
                               config,
                               option,
                               OPTIONS[option])

    return global_configuration
