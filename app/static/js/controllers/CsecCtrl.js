app.controller('CsecCtrl',['$scope','subjectList','$http','$location', function($scope,subjectList,$http,$location){
	
	if(localStorage.userID == null){
		$location.url("/")
	}

	subjectList.csecList().then(function(response){
		// console.log(data);
		$scope.subjects = response.data
	});

	$scope.grades = ["I","II","III","IV","V","VI","U"]

	$scope.studied=[]

	

	$scope.addSubject = function(){
		$scope.studied.push({})
		console.log($scope.studied)
		if($scope.studied.length ==0){
			$scope.allowSubmit = false
		}
		else{
			$scope.allowSubmit = true
		}
	}

	$scope.submitSubs = function(){
		data = $scope.studied
		$http.post('/api/submit/'+localStorage.userID,data,{

				headers:{'Content-Type':"csec-subjects"}

			}).then(function(response){
				if(response.data.status =="success"){
					$location.url("/home")
				}else{
					console.log( response.data.message)
				}
				
			})
		}
}]);