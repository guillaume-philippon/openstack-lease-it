angular.module('leaseItAuth').
    factory('$leaseItAuth', function() {
        /* By default, we are not authenticate and we are not administrator */
        var authenticated = false;
        var administrator = false;

        return {
            /* authenticate user to backend */
            authenticate: function (username, password, domain) {
                if (! authenticated ) {
                    authenticated = true;
                } else {
                    authenticated = false;
                }
            },
            /* logout user */
            logout: function () {
                authenticated = false;
            },
            is_authenticated: function (){
                return authenticated;
            },
            is_admin: function (){
                return administrator;
            }
        }
    });