$(document).ready(function() {
	var table = $("#voter_table").DataTable( {
		"processing": true,
		"serverSide":  true,
		"ajax":"voter_json/",	
		// "deferRender": true,
		"columnDefs": [
			{
				"render": function(data, type, row) {
					console.log(data);
					return "<input type='checkbox' class='signatureCheck' data-voteid='"+ row[0] +"' " + (data ? "checked" : "") + " />"; 
				},
				"targets": 14
			}
		]
	});


	$(document).on('change', '.signatureCheck', function(){
		var voteid = $(this).data("voteid");
		var checked =  $(this).is(":checked");
		console.log(checked);
		$.post("voter_signature/", {"voteID": voteid, "checked": checked, "csrfmiddlewaretoken":'{{csrf_token}}'},   function(data){
			console.log("updated");
		});
	});
});





     
