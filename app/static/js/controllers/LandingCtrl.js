app.controller('LandingCtrl', ['$scope','$http','$location', function($scope,$http,$location){
	if(localStorage.userID != null){
		// $scope.showNav = true
		$location.url("/home")
	}
	// $scope.showNav = false

}])