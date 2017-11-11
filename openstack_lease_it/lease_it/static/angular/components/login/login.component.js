angular.module('leaseItLogin').
    component('leaseItLogin', {
        templateUrl: 'components/login/login.template.html',
        controller: function LeaseItLogin($scope, $leaseItAuth, $window) {

            /* if we are already authenticated, then we redirect to /dashboard */
            if ($leaseItAuth.is_authenticated()) {
                $window.location.href = '#!/dashboard';
            };

            /* login function for controller leaseItLogin */
            this.login = function () {
                /* We call $leaseItAuth service with the form parameter */
                $leaseItAuth.
                    authenticate($scope.username, $scope.password, $scope.domain);
                /* when, we are logged, we redirect to /dashboard*/
                $window.location.href = '#!/dashboard';
            };
        }
    });