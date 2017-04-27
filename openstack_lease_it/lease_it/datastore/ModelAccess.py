# -*- coding: utf-8 -*-


class ModelAccess(object):
    """
       ModelAccess is a class will abstract model access for application. It will get / save / ... informations in
       a format expected by views
    """
    def __init__(self):
        super(ModelAccess, self).__init__()
