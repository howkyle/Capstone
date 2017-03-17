var app =angular.module("SubjectSelectionApp", []);

app.controller('CsecCtrl',['$scope', function($scope){
	$scope.subjects = ["Mathematics","Additional Mathematics","Biology", "Chemistry","Physics","Technical Drawing","French","Spanish","Art","Information Technology"]
	$scope.grades = ["I","II","III","IV","V","VI","U"]
}])


app.controller('CapeCtrl', ['$scope', function($scope){
	$scope.test = "Nice Day"
	console.log($scope.test)
	 
}])