app.controller('CapeCtrl', ['$scope', 'subjectList','$http','$location',function($scope,subjectList,$http,$location){
	subjectList.capeList().then(function (response) {
		$scope.subjects = response.data
		console.log($scope.subjects)

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
					console.log("herereeerer")
					console.log( response.data.message)
					$location.url("/home")
				}else{
					console.log("herereeerer")
					console.log( response.data.message)
				}
			})
		}
	})
}]);