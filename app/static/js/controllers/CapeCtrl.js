app.controller('CapeCtrl', ['$scope', 'subjectList','$http','$location',function($scope,subjectList,$http,$location){
	subjectList.capeList().then(function (response) {
		$scope.subjects = response.data

		$scope.applied=[]

		$scope.addSubject = function(){
			$scope.applied.push({})
			console.log($scope.applied)
		}

		$scope.submitSubs = function(){
		data = $scope.applied
		$http.post('/api/submit/'+localStorage.userID,data,{

				headers:{'Content-Type':"cape-subjects"}

			}).then(function(response){
				if(response.data.status =="success"){
					$location.url("/home")
				}else{
					console.log( response.data.message)
				}
			})
		}
	})
}]);