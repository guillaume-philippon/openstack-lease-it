# -*- coding: utf-8 -*-
"""
ModelAccess module is a interface between Django model and view
"""


class ModelAccess(object):  # pylint: disable=too-few-public-methods
    """
    ModelAccess is a class will abstract model access for application. It
    will get / save / ... informations in a format expected by views
    """
