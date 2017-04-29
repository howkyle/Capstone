app.controller('HomeCtrl', ['$scope','$http','$location', function($scope,$http,$location){
	if(localStorage.userID == null){
		$location.url("/")
	}
	// $scope.showNav = true
	// console.log("homeeeeeeee bitch")
}])