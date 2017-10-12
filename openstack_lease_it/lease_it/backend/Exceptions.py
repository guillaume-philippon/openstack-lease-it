"""
This module contains all exception triggered by Backend
"""


class PermissionDenied(Exception):
    """
    PermissionDenied exception is triggered when a user (logged or not) try to make an invalid
    command
    """
    def __init__(self, user_id, instance_id):
        super(PermissionDenied, self).__init__()
        self.message = "User {} is not authorized to update status of instance {}".format(
            user_id, instance_id)
