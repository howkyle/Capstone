app.factory('submitSubjects', ['$http', function($http){

	return {

		submitCsec : function(data){

			console.log(data)

			$http.post('/profile',data,{

				headers:{'Content-Type':"csec-subjects"}

			})

		},
		submitCape : function(data){

			$http.post('/profile',data,{

				headers:{'Content-Type':"cape-subjects"}

			})

		}
	}

}])