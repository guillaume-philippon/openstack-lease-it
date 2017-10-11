# openstack-lease-it
OpenStack lease-it add some useful feature to monitor a OpenStack instances
 * Display the list of flavor and display the number of instance we can create with this
 flavor
 * Add a **lease** feature to OpenStack that force user to renew a lease to keep instance
  running. If a lease expire, the instance is killed

## Installation
#### Installation dependencies (CentOS 7.x)
```shell
box# easy_install pip
box# yum install -y gcc python-devel openldap-devel memcached httpd mod_wsgi mod_ssl git
box# systemctl enable memcached httpd
box# systemctl start memcached httpd
```

#### Install openstack-lease-it and dependencies with pip
```shell
box# cd /opt
box# git clone https://github.com/LAL/openstack-lease-it.git
box# cd openstack-lease-it
box# pip install -r requirements.txt
```

#### Configuration file and test
```shell
box# mkdir -p /etc/openstack-lease-it
box# cp openstack_lease_it/lease-it.cfg.example /etc/openstack-lease-it/config.ini
```
Modify `/etc/openstack-lease-it/config.ini to match your configuration. You must also need to 
disabled selinux to allow apache to read /etc/openstack-lease-it/config.ini or configure it to allow
 that.

You must modify `/opt/openstack-lease-it/openstack_lease_it/openstack_lease_it/settings.py` to change
```ini
ALLOWED_HOSTS = [ '*' ]
```

#### Configure database
By default, we use sqlite3 database. to populate it
```shell
box# cd /opt/openstack-lease-it/openstack_lease_it
box# python manage.py makemigrations
box# python manage.py migrate
box# chown -R apache:apache .
```

#### Configure Apache
We put apache config on `/etc/httpd/conf.d/lease-it.conf`
```apache
WSGIScriptAlias / /opt/openstack-lease-it/openstack_lease_it/openstack_lease_it/wsgi.py
#WSGIPythonHome /path/to/venv
WSGIPythonPath /opt/openstack-lease-it/openstack_lease_it

Alias /static/ /opt/openstack-lease-it/openstack_lease_it/lease_it/static/ 
Alias /media/ /opt/openstack-lease-it/openstack_lease_it/lease_it/media/

<Directory /opt/openstack-lease-it/openstack_lease_it/openstack_lease_it/>
  <Files wsgi.py>
    Require all granted
  </Files>
</Directory>

<Directory /opt/openstack-lease-it/openstack_lease_it/lease_it/static/>
  Require all granted
</Directory>

<Directory /opt/openstack-lease-it/openstack_lease_it/lease_it/media/>
  Require all granted
</Directory>
```

After apache configuration you must restart httpd service with the following command
```shell
box# systemctl restart httpd
```

#### Instance-spy crontab
To monitor instances and notify user when a instance is close to expire, we use a crontab. To do
so, put the cron script to cron directory
```shell
box# cp openstack_lease_it/instance-spy.cron /etc/cron.weekly/
box# chmod +x /etc/cron.weekly/instance-spy.cron
```

Make sure that the PYTHONPATH on script is in the right place. This script should also be modified 
if you use virtualenv