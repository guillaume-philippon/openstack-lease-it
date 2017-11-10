angular.module('leaseIt').
    config(['$locationProvider', '$routeProvider',
        function config($locationProvider, $routeProvider){
            $locationProvider.hashPrefix('!');

            $routeProvider.
                when('/login',{
                    template: '<lease-it-login></lease-it-login>'
                }).
                when('/dashboard', {
                    template: '<lease-it-dashboard><lease-it-dashboard>'
                }).
                otherwise('/login')
        }]);