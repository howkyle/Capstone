app.controller('CapeCtrl', ['$scope', 'subjectList','$http','$location',function($scope,subjectList,$http,$location){
	subjectList.capeList().then(function (response) {
		$scope.subjects = response.data
		console.log($scope.subjects)
	})

	subjectList.applied().then(function(response){
		$scope.capeApplied = response.data.data
		console.log(response.data)
		if (($scope.capeApplied.length) <=4){
		$scope.disableAdd = false
		}else{
			$scope.disableAdd =true
		}
	})
	$scope.applied=[]

	
	

	$scope.addSubject = function(){

		$scope.applied.push({})
		if($scope.applied.length ==0){
			$scope.allowSubmit = false
		}
		else{
			$scope.allowSubmit = true
		}
		console.log($scope.applied)
		console.log($scope.applied.length + $scope.capeApplied.length)
		if (($scope.applied.length + $scope.capeApplied.length) >=4){
			$scope.disableAdd = true

		}
	}


	$scope.submitSubs = function(){
		data = $scope.applied
		$http.post('/api/submit/'+localStorage.userID,data,{

			headers:{'Content-Type':"cape-subjects"}

		}).then(function(response){
			if(response.data.status =="success"){
				// console.log("herereeerer")
				// console.log( response.data.message)
				$location.url("/home")
			}else{
				// console.log("herereeerer")
				console.log( response.data.message)
			}
		})
	}
	
}]);