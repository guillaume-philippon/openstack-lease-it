angular.module('leaseItDotRemove').
    filter('leaseItDotRemove', function (){
        return function (item) {
            return item.replace(/\./g, '');
        }
    })