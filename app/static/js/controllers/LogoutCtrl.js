app.controller('LogoutCtrl', ['$scope','$http','$location', function($scope,$http,$location){
	localStorage.removeItem("userID")
	localStorage.removeItem("fname")
	localStorage.removeItem("lname")
	$location.url('/')
}])