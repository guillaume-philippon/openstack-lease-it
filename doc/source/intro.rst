Introduction
============

OpenStack lease it is a tools that add some usefull features to a OpenStack infrastructure. It
currently have two major features:

* Flavors: which provide the list of flavors available on OpenStack and, for each of it, provide the number of instances that can be started in the current cloud infrastructure state. It s a kind of "cloud's weather" tools
* Instances: which monitor the current running instances and put a "lease" on it (90 days lease), notify user when the lease will expire and
