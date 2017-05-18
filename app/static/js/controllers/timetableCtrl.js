app.controller('timetableCtrl', ['$scope', 'subjectList','$http','$location',function($scope,subjectList,$http,$location){
	if(localStorage.userID == null){
		$location.url("/")
	}
	else{
		if(localStorage.userID == 'admin'){
			$location.url('/admin')
		}
	}

	subjectList.timeTable().then(function(response){
		console.log(response.data)
		$scope.subjects = response.data
	})

}])