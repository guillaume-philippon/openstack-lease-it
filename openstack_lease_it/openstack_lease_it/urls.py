"""openstack_lease_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from openstack_lease_it.settings import GLOBAL_CONFIG

if GLOBAL_CONFIG['BACKEND_PLUGIN'] == 'Openstack':
    urlpatterns = [  # pylint: disable=invalid-name
        # openstack_auth.urls provide login & logout view plus some more usefull stuff
        # templates should be placed into templates/auth/ (login.html / logout.html)
        url(r'^', include('openstack_auth.urls')),

        # import all lease_it urls
        # TODO: Perhaps 2 specific app for lease-it and flavors listing
        url(r'^', include('lease_it.urls'))
    ]
else:
    urlpatterns = [  # pylint: disable=invalid-name
        url(r'^login', 'openstack_lease_it.views.login', name='login'),
        url(r'^logout', 'openstack_lease_it.views.logout', name='logout'),
        url(r'^', include('lease_it.urls'))
    ]
