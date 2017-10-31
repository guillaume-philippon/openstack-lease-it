"""
This module contains all exception triggered by Backend
"""


class StillRunning(Exception):
    """
    PermissionDenied exception is triggered when a user (logged or not) try to make an invalid
    command
    """
    def __init__(self, instance_id, heartbeat):
        super(StillRunning, self).__init__()
        self.message = "Instance {} is still running {}".format(
            instance_id, heartbeat)
