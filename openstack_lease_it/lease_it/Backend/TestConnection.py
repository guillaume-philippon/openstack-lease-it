#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-


class TestConnection(object):
    def __init__(self):
        super(TestConnection, self).__init__()

    def instances(self):
        return {}

    def usage(self):
        return {
            'm1.small': {
                'name': 'm1.small',
                'disk': 10,
                'ram': 1024,
                'cpu': 1,
                'free': 50,
                'max': 100,
            }
        }
