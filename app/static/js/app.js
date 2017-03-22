var app =angular.module("SubjectSelectionApp", []);

app.controller('CsecCtrl',['$scope','csecList', function($scope,csecList){
	// $scope.subjects = ["Mathematics","Additional Mathematics","Biology", "Chemistry","Physics","Technical Drawing","French","Spanish","Art","Information Technology"]
	csecList.success(function(data){
		console.log(data);
		$scope.subjects = data
	});
	$scope.grades = ["I","II","III","IV","V","VI","U"]
}]);


app.controller('CapeCtrl', ['$scope', function($scope){
}])
	
	 
