angular.module('leaseItDotRemove').
    filter('leaseItDotRemove', function (){
        return function (item) {
            console.log('item: ' + item.replace(/\./g, ""))
            return item.replace(/\./g, '');
        }
    })