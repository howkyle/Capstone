app.controller('adminCtrl', ['$scope','subjectList','$http','$location',function($scope,subjectList,$http,$location){
	
	subjectList.capeList().then(function(response) {
		$scope.capeList = response.data
		console.log($scope.subjects)
	})

	$http.get('/api/config').then(function(response){
		if (response.data){
			$scope.mandatorySubject = response.data.mandatory
			$scope.classSize = response.data.classSize
		}
	})

	$http.get('/api/admin/students').then(function(response){
		$scope.students = response.data
		$scope.acceptedStudents = []
		$scope.rejectedStudents =[]
		for(i =0;i< $scope.students.length;i++){
			console.log($scope.students[i].id)
			if ($scope.students[i].subjects.length<4){
				$scope.rejectedStudents.push($scope.students[i])
			}else{
				$scope.acceptedStudents.push($scope.students[i])
			}
		}

		$scope.displayConfig = false
		$scope.showConfig = function(){
			$scope.displayConfig = true
		}

		$scope.saveConfig = function(){
			$scope.displayConfig = false
			url = '/api/config'
			data = {
				"mandatory":$scope.mandatorySubject.name,
				"classSize":$scope.classSize
			}
			$http.post(url, data).then(function(response){
				$scope.mandatorySubject = response.data.mandatory
				$scope.classSize = response.data.classSize
			})
		}
	})

	


}])