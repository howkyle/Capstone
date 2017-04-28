app.controller('CapeCtrl', ['$scope', 'subjectList','submitSubjects',function($scope,subjectList,submitSubjects){
	subjectList.capeList().then(function (response) {
		$scope.subjects = response.data

		$scope.applied=[]

		$scope.addSubject = function(){
			$scope.applied.push({})
			console.log($scope.applied)
		}

		$scope.submitSubs = function(){
		data = $scope.applied
		submitSubjects.submitCape(data)
	}
	})
}]);