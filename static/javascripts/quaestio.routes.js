/**
 * Created by Bahrom on 1/7/16.
 */
(function() {
    'use strict';

    angular
        .module('quaestio.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */

    function config($routeProvider) {
        $routeProvider.when(
            '/register', {
                controller: 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/register.html'
            }
        ).otherwise('/');
    }
})();