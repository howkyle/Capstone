app.factory('submitSubjects', ['$http', function($http){

	return {

		submitCsec : function(data){

			// console.log(data)

			$http.post('/api/submit/'+localStorage.userID,data,{

				headers:{'Content-Type':"csec-subjects"}

			}).then(function(response){
				console.log("HREREEEEEEE")
				return response
			})

		},
		submitCape : function(data){

			$http.post('/api/submit/'+localStorage.userID,data,{

				headers:{'Content-Type':"cape-subjects"}

			})
		}
	}

}])