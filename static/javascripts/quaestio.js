/**
 * Created by Bahrom on 1/7/16.
 */
angular
  .module('quaestio', []);

(function() {
    'use strict';

    angular
        .module('quaestio', [
            'quaestio.config',
            'quaestio.routes',
            'quaestio.authentication'
        ]);

    angular
        .module('quaestio.config', []);

    angular
        .module('quaestio.routes', ['ngRoute']);
})();