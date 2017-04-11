from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'lease_it.views.dashboard', name='dashboard'),
    url(r'^flavors', 'lease_it.views.flavors', name='flavors')
]