app.controller('HeaderCtrl', ['$scope', function($scope){
	if(localStorage.userID != null){
		$scope.userID = localStorage.userID
		$scope.fname = localStorage.fname
		$scope.lname = localStorage.lname
		$scope.showNav = true
		console.log("show the nav")
	}
	else{
		$scope.showNav=false
		console.log("dont show the nav")
	}
}])


// remove this controller