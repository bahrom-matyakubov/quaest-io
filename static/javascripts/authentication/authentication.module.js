/**
 * Created by Bahrom on 1/7/16.
 */

(function() {
    'use strict';

    angular
        .module('quaestio.authentication', [
            'quaestio.authentication.controllers',
            'quaestio.authentication.services'
        ]);

    angular
        .module('quaestio.authentication.controllers', []);

    angular
        .module('quaestio.authentication.services', ['ngCookies']);
})();