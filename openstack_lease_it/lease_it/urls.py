from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'lease_it.views.dashboard', name='dashboard'),
    url(r'^flavors', 'lease_it.views.flavors', name='flavors')
]