/**
 * Created by Bahrom on 1/7/16.
 */
/**
* Authentication
* @namespace quaestio.authentication.services
*/
(function() {
    'use strict';

    angular
        .module('quaestio.authentication.services')
        .factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    /**
     * @namespace Authentication
     * @returns {Factory}
     */
    function Authentication($cookies, $http) {
        /**
         * @name Authentication
         * @desc The Factory to be returned
         */
        var Authentication = {
            register: register
        };
        return Authentication;

        ////////////////

        /**
         * @name register
         * @desc try to register a new user
         * @param {string} username The username entered
         * @param {string} password The password entered
         * @param {string} email The email entered
         * @returns {Promise}
         * @memberOf quaestio.authentication.services.Authentication
         */

        function register(email, password, username) {
            return $http.post('/api/v1/accounts/', {
                username: username,
                password: password,
                email: email
            });
        }
    }
})();