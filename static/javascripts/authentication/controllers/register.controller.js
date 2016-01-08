/**
 * Created by Bahrom on 1/7/16.
 */

/**
 * Register controller
 * @namespace quaestio.authentication.controllers
 */
(function() {
    'use strict';

    angular
        .module('quaestio.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    /**
     * @namespace RegisterController
     */

    function RegisterController($location, $scope, Authentication) {
        var vm = this;

        vm.register = register;

        /**
         * @name register
         * @desc Register a new user
         * @memberOf quaestio.authentication.controllers.RegisterController
         */
        function register() {
            Authentication.register(vm.email, vm.password, vm.username);
        }
    }
})();
