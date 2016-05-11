$(document).ready(function() {
	var table = $("#voter_table").DataTable( {
		"processing": true,
		"serverSide":  true,
		"ajax":"voter_json/",	
		"deferRender": true,
	});
});