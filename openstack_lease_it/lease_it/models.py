# pylint: skip-file
"""
model for django database. Use for 2 differents cases:
* Cache some data to avoid useless overload on OpenStack infrastructure
   - instances informations
   - user informations
   - ...
* Store data that is not available on OpenStack
   - lease time
   - ...
"""
from django.db import models


class Instances(models.Model):
    """
    Instance model will be use to store instances informations
    as id / name / launch time / lease time / ...
    """
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    created_at = models.DateField()  # Date when VM as been started
    heartbeat_at = models.DateField()  # Last time we've see this instances
    leased_at = models.DateField()  # Date for last lease
    lease_duration = models.IntegerField()  # Lease duration (month)


class UserInformation(models.Model):
    """
    This class store extra information about user. It s not
    a extension of User model as openstack_auth use a different
    version that can be tricky to merge
    """
    id = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

