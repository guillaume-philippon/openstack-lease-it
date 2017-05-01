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
    id = models.CharField(primary_key=True, max_length=50)  # Instance id all other data could be modify
    heartbeat_at = models.DateField()  # Last time we've see this instances
    leased_at = models.DateField()  # Date for last lease
    lease_duration = models.IntegerField()  # Lease duration (month)
