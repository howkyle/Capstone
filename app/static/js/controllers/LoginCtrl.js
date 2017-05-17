app.controller('LoginCtrl', ['$scope','$http','$location', function($scope,$http,$location){

	if(localStorage.userID != null){
		if(localStorage.userID == 'admin'){
			$location.url('/admin')
		}else{
			// $scope.showNav = true
		$location.url("/home")
		}
		
	}
	// $scope.showNav = false	

	$scope.login = function(){
		url = '/api/login'
		newLocation = '/home'

		config = {
			headers:{
				"Content-Type":"application/json"
			}
		}

		data = {
			"id":$scope.studentID,
			"password":$scope.password
		}

		if($scope.adminCheck){
			url = '/api/admin/login'
			newLocation ='/admin'
			data = {
			"id":$scope.studentID,
			"password":$scope.password
				}

		}

		$http.post(url, data, config).then(function(response){
			if(response.data.status =="success"){
				console.log(response.data)
				localStorage.setItem("userID",response.data.data.id)
				localStorage.setItem("fname",response.data.data.fname)
				localStorage.setItem("lname",response.data.data.lname)
				$scope.logged = true

				$location.url(newLocation)
			}
			else{
				console.log(response.data.message)
			}
		})

	}
}])