/* Make sure javascript code is *clean* as far as it can be */
'use strict';

/* load app module for angularJS */
var leaseIt = angular.module('leaseIt', [
    'ngRoute',
    'ui.materialize',
    'leaseItNavbar',
    'leaseItLogin',
    'leaseItDashboard'
]);