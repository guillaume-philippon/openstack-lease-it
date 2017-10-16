# coding: utf-8
"""
This module define a list of homemade decorators
"""
from django.core.exceptions import PermissionDenied


def superuser_required(view):
    """
    If superuser access is required for a specific view, we use
    @superuser_required decorator
    :param view: As parameter, we have the view function
    :return: function
    """
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = view.__doc__
    wrap.__name__ = view.__name__
    return wrap
