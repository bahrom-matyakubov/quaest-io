/**
 * Created by Bahrom on 1/8/16.
 */
(function() {
    'use strict';

    angular
        .module('quaestio.config')
        .config(config);

    config.$inject = [$locationProvider];

    /**
     * @name config
     * @desc Enable HTML5 routing
     */
    function config($locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
    }
})();