# -*- coding: utf-8 -*-
"""
ModelAccess module is a interface between Django model and view
"""

from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from lease_it.models import Instances

# Default lease duration
LEASE_DURATION = 3


class InstancesAccess(object):  # pylint: disable=too-few-public-methods
    """
    ModelAccess is a class will abstract model access for application. It
    will get / save / ... informations in a format expected by views
    """
    @staticmethod
    def show(instances):
        """
        Return a list of instances store on database
        :return: dict of instances
        """
        response = dict()
        for instance in instances:
            try:
                models = Instances.objects.get(id=instances[instance]['id'])  # pylint: disable=no-member
                leased_at = models.leased_at
                heartbeat_at = models.heartbeat_at
                lease_end = leased_at + relativedelta(months=+models.lease_duration)
            except ObjectDoesNotExist:
                leased_at = None
                heartbeat_at = None
                lease_end = None

            response[instances[instance]['id']] = {
                'name': instances[instance]['name'],
                'id': instances[instance]['id'],
                'user_id': instances[instance]['user_id'],
                'project_id': instances[instance]['project_id'],
                'created_at': instances[instance]['created_at'],
                'leased_at': leased_at,
                'heartbeat_at': heartbeat_at,
                'lease_end': lease_end
            }
        return response

    @staticmethod
    def save(instances):
        """
        Store all instances or update it
        :param instances: dict of instances to save
        :return: void
        """
        for instance in instances:
            # Retrieve current instance data if available
            try:
                model = Instances.objects.get(id=instances[instance]['id'])  # pylint: disable=no-member
            except ObjectDoesNotExist:
                # If not, then we create a new entry with information from instances
                model = Instances()
                model.id = instances[instance]['id']
            model.leased_at = timezone.now()
            model.lease_duration = LEASE_DURATION
            model.heartbeat_at = timezone.now()
            model.save()
