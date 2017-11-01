Introduction
============

OpenStack lease it is a tools that add some usefull features to a OpenStack infrastructure. It
currently have two major features:

* Flavors: which provide the list of flavors available on OpenStack and, for each of it, provide the number of instances that can be started in the current cloud infrastructure state. It s a kind of "cloud's weather" tools
* Instances: which monitor the current running instances and put a "lease" on it (90 days lease), notify user when the lease will expire and

Credits
-------

We use some set of framework and toolkit provided by community, included

For web interface:

* jQuery_
* materializeCSS_
* HighCharts_
* DataTables_

Some of this tools (`HighCharts Licence <https://shop.highsoft.com/highcharts/>`_) need some specific licencing depending the usage.

For backend:

* Django_
* Openstack_
* Sphinx_

.. _jQuery: https://jquery.com/
.. _materializeCSS: http://materializecss.com/
.. _DataTables: https://datatables.net
.. _HighCharts: https://www.highcharts.com
.. _Django: https://www.djangoproject.com/
.. _Openstack: http://www.openstack.org
.. _Sphinx: http://www.sphinx-doc.org/