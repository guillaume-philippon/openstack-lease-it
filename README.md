# openstack-lease-it
Monitor OpenStack virtual machine age and kill it if the bail expire

## Installation
#### Installation dependencies (CentOS 7.x)
```
box# easy_install pip
box# yum install gcc python-devel openldap-devel memcached httpd mod_wsgi
box# systemctl enable memcached httpd
box# systemctl start memcached httpd
```

#### Install openstack-lease-it and dependencies with pip
```
box# cd /opt
box# git clone https://github.com/LAL/openstack-lease-it.git
box# cd openstack-lease-it
box# pip install -r requirements.txt
```

#### Configuration file and test
```
box# mkdir -p /etc/openstack-lease-it
box# cp lease-it.cfg.example /etc/openstack-lease-it/config.ini
```
Modify /etc/openstack-lease-it/config.ini to match your configuration. You must also need to disabled selinux to
allow apache to read /etc/openstack-lease-it/config.ini or configure it to allow that.

You must modify ```/opt/openstack-lease-it/openstack_lease_it/openstack_lease_it/settings.py``` to change
```
ALLOWED_HOSTS = [ '*' ]
```

#### Configure Apache
```
box# cat /etc/httpd/conf.d/lease-it.conf
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
box# systemctl restart httpd
```