app.controller('LandingCtrl', ['$scope','$http','$location', function($scope,$http,$location){
	if(localStorage.userID != null){
		if(localStorage.userID == 'admin'){
			$location.url('/admin')
		}else{
			// $scope.showNav = true
		$location.url("/home")
		}
	}
	// $scope.showNav = false

}])