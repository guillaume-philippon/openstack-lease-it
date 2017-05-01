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
    def instances():
        """
        Return a list of instances store on database
        :return: dict of instances
        """
        instances = Instances.objects.all()  # pylint: disable=no-member
        response = dict()
        for instance in instances:
            response[instance.id] = {
                'name': instance.name,
                'id': instance.id,
                'created_at': instance.created_at,
                'leased_at': instance.leased_at,
                'heartbeat_at': instance.heartbeat_at,
                'lease_end': instance.leased_at + relativedelta(months=+instance.lease_duration)
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
                model.created_at = instances[instance]['created_at']
                model.leased_at = timezone.now()
                model.lease_duration = LEASE_DURATION

            # We update instance name if changed
            model.name = instances[instance]['name']

            # Last update for this object
            model.heartbeat_at = timezone.now()
            instances[instance]['heartbeat_at'] = model.heartbeat_at

            # If instances there are leased_at information on instance, then we must update the
            # model information. Else, we put leased_at information on instance
            try:
                model.leased_at = instances[instance]['leased_at']
            except KeyError:
                instances[instance]['leased_at'] = model.leased_at

            # If we send a lease_duration with instance, we update lease duration
            try:
                model.lease_duration = instances[instance]['lease_duration']
            except KeyError:
                pass

            # We compute lease_end to be available on instance
            instances[instance]['lease_end'] = model.leased_at +\
                                               relativedelta(months=+model.lease_duration)

            # We save the model
            model.save()
