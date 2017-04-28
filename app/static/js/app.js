var app =angular.module("SubjectSelectionApp", ['ngRoute']);

app.config(['$routeProvider',function($routeProvider) {
	$routeProvider
	.when('/',{
		templateUrl: 'static/js/views/landing.html',
		controller: 'LandingCtrl'
	})
	.when('/login',{
		templateUrl: 'static/js/views/login.html',
		controller: 'LoginCtrl'
	})
	.when('/home',{
		templateUrl: 'static/js/views/home.html',
		controller:'HomeCtrl'
	})
	.when('/csec',{
		templateUrl:'static/js/views/csec.html',
		controller:'CsecCtrl'
	})
	.when('/cape',{
		templateUrl:'static/js/views/cape.html',
		controller: 'CapeCtrl'
	})
	.when('/register',{
		templateUrl:'static/js/views/register.html',
		controller:'RegisterCtrl'
	})
	.otherwise({
		redirectTo:'/'
	})
}])





	
	 
