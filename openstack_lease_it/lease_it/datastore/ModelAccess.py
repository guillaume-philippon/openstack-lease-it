# -*- coding: utf-8 -*-
"""
ModelAccess module is a interface between Django model and view
"""

from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from lease_it.models import Instances
from openstack_lease_it.settings import LOGGER_INSTANCES

# Default lease duration in day
LEASE_DURATION = 90


class InstancesAccess(object):  # pylint: disable=too-few-public-methods
    """
    ModelAccess is a class will abstract model access for application. It
    will get / save / ... informations in a format expected by views
    """
    @staticmethod
    def get(instance):
        """
        Get or Create instance on model backend
        :param instance: instance to get
        :return: Instance model
        """
        try:
            model = Instances.objects.get(id=instance['id'])  # pylint: disable=no-member
        except ObjectDoesNotExist:
            LOGGER_INSTANCES.info('Instance %s as never been seen before', instance['id'])
            model = Instances()
            model.id = instance['id']
            model.leased_at = timezone.now()
            model.heartbeat_at = timezone.now()
            model.lease_duration = LEASE_DURATION
        return model

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
                lease_end = leased_at + relativedelta(days=+models.lease_duration)
            except ObjectDoesNotExist:
                LOGGER_INSTANCES.info("Instance %s not exists", instance)
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
    def heartbeat(instance):
        model = InstancesAccess.get(instance)
        model.heartbeat_at = timezone.now()
        model.save()
        LOGGER_INSTANCES.info('Instance %s as been heartbeated (%s)', model.id, model.heartbeat_at)

    @staticmethod
    def lease(instance):
        model = InstancesAccess.get(instance)
        model.leased_at = timezone.now()
        model.save()
        LOGGER_INSTANCES.info('Instance %s as been leased (%s)', model.id, model.heartbeat_at)
