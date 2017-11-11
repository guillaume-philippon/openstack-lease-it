angular.module('leaseItNavbar').
    component('leaseItNavbar', {
        templateUrl: 'components/navbar/navbar.template.html',
        controller: function LeaseItNavbarController ($scope, $leaseItAuth){

            /* ask $leaseItAuth to know the authenticate status of user */
            $scope.is_authenticated = $leaseItAuth.is_authenticated();
            $scope.is_admin = true;

            /* We watch is_authenticated status to see if it change */
            $scope.$watch($leaseItAuth.is_authenticated, function (){
                /* So, we update the scope status */
                $scope.is_authenticated = $leaseItAuth.is_authenticated()
            })
        }
    });