# openstack-lease-it
Monitor OpenStack virtual machine age and kill it if the bail expire

## Installation
#### Installation dependencies (CentOS 7.x)
```
box# easy_install pip
box# yum install gcc python-devel openldap-devel
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
Modify /etc/openstack-lease-it/config.ini to match your configuration