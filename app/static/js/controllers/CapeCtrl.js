app.controller('CapeCtrl', ['$scope', 'subjectList','$http','$location',function($scope,subjectList,$http,$location){
	
	if(localStorage.userID == null){
		$location.url("/")
	}
	else{
		if(localStorage.userID == 'admin'){
			$location.url('/admin')
		}
	}
	
	subjectList.capeList().then(function(response) {
		$scope.subjects = response.data
		
	})

	$http.get('/api/config').then(function(response){
		if (response.data){
			$scope.mandatorySubject = response.data.mandatory
			$scope.classSize = response.data.classSize
			for (i =0;i<$scope.subjects.length;i++){
				if($scope.subjects[i].name == $scope.mandatorySubject){
					$scope.subjects.splice(i,1)
					break
				}
			}
		}
	})

	

	subjectList.applied().then(function(response){
		$scope.capeApplied = response.data.data
		// console.log(response.data)
		if (($scope.capeApplied.length) <=4){
		$scope.disableAdd = false
		}else{
			$scope.disableAdd =true
		}
	})
	$scope.applied=[]

	
	

	$scope.addSubject = function(){

		$scope.applied.push({})
		if($scope.applied.length==0){
			$scope.allowSubmit = false
		}
		else{
			$scope.allowSubmit = true
		}
		// console.log($scope.applied)
		// console.log($scope.applied.length + $scope.capeApplied.length)
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