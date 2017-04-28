app.controller('CsecCtrl',['$scope','subjectList','submitSubjects', function($scope,subjectList,submitSubjects){
	
	subjectList.csecList().then(function(response){
		// console.log(data);
		$scope.subjects = response.data
	});

	$scope.grades = ["I","II","III","IV","V","VI","U"]

	$scope.studied=[]

	$scope.addSubject = function(){
		$scope.studied.push({})
		console.log($scope.studied)
	}

	$scope.submitSubs = function(){
		data = $scope.studied
		submitSubjects.submitCsec(data)
	}
}]);