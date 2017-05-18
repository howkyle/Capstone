// app.factory('csecList', ['$http', function($http){
// 	return $http.get('/profile', { 
// 		headers : { 'Accept': "csec-list"} //request the list of csec subjects from flask database
// })
// 	.success(function(data){
// 		return data
// 	})
// 	.error(function(data){
// 		return "csec list error"
// 	})
// }])

app.factory('subjectList', ['$http', function($http){

	return{		
			capeList:function(data){
				return $http.get('/api/subjects', { 
					headers : { 'Accept': "cape-list"}
				})
			},

			csecList:function(data){
				return $http.get('/api/subjects', { 
					headers : { 'Accept': "csec-list"} //request the list of csec subjects from flask database
				})
			},
			studied:function(data){
				return $http.get('/api/subjects/'+localStorage.userID,{
					headers:{'Accept':'csec'}
				})
			},
			applied:function(data){
				return $http.get('/api/subjects/'+localStorage.userID,{
					headers:{'Accept':'cape'}
				})
			},
			successfulCape:function(data){
				return $http.get('/api/subjects/'+localStorage.userID,{
					headers:{'Accept':'successful-cape'}
				})
			},
			timeTable:function(data){
				return $http.get('/api/timetable/'+localStorage.userID)
			}

	}
		
}])