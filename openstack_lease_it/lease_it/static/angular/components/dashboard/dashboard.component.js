angular.module('leaseItDashboard').
    component('leaseItDashboard', {
        templateUrl: 'components/dashboard/dashboard.template.html',
        controller: function leaseItDashboard ($scope, $leaseItAuth, $window) {
            $scope.showTabs = true;
            if (! $leaseItAuth.is_authenticated()) {
                $window.location.href = '#!/login';
            }
        }
    });