app.controller('HomeCtrl', ['$scope','$http','$location','subjectList', function($scope,$http,$location,subjectList){
	if(localStorage.userID == null){
		$location.url("/")
	}

	// $scope.message = "Find out next time on dragon ball z"
	
	subjectList.studied().then(function(response){
		$scope.csecSubmitted = response.data.data
		console.log(response.data)
	})

	subjectList.applied().then(function(response){
		$scope.capeApplied = response.data.data
		console.log(response.data)
	})

	subjectList.successfulCape().then(function(response){
		$scope.successfulCape = response.data.data
		if($scope.successfulCape.length==0){
			$scope.message = "Find out next time on dragon ball z"
			$scope.showMessage = true
		}
		else if($scope.successfulCape.length<4){
			$scope.message = "No place available for you"
			$scope.showMessage = true
		}
		else{
			$scope.showMessage = false
		}
		console.log(response.data)
	})
}])