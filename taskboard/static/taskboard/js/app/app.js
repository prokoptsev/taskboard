var app = angular.module('TaskBoardApp', [
    'ngCookies'
]).config(function($httpProvider, $interpolateProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}).run(function($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
    // Add the following two lines
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
});
