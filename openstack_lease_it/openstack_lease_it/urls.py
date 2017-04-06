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
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', 'openstack_lease_it.views.logout', name='logout'),
    url(r'^login$', 'openstack_lease_it.views.login', name='login'),
    url(r'^home$', 'openstack_lease_it.views.home_dispatcher', name='home_dispatcher'),
    url(r'^$', 'openstack_lease_it.views.home_dispatcher', name='home_dispatcher'),
    url(r'^test$', 'openstack_lease_it.views.hypervisor_dispatcher', name='hypervisor_dispatcher'),
    # url(r'^', include('lease_it.urls')),
]
