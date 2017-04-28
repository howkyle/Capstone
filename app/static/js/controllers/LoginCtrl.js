app.controller('LoginCtrl', ['$scope','$http','$location', function($scope,$http,$location){

	if(localStorage.userID != null){
		$location.url("/home")
	}	

	$scope.login = function(){
		url = '/api/login'
		config = {
			headers:{
				"Content-Type":"application/json"
			}
		}

		data = {
			"id":$scope.studentID,
			"password":$scope.password
		}

		$http.post(url, data, config).then(function(response){
			if(response.data.status =="success"){
				console.log(response.data)
				localStorage.setItem("userID",response.data.data.id)
				localStorage.setItem("fname",response.data.data.fname)
				localStorage.setItem("lname",response.data.data.lname)
				$location.url('/home')
			}
			else{
				console.log(response.data.message)
			}
		})

	}
}])