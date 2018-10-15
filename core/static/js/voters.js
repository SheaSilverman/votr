$(document).ready(function() {
	console.log("Loaded lets go");

	$('#voter_table tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    } );
 
	
	var table = $("#voter_table").DataTable( {
		"processing": true,
		"serverSide":  true,
		"ajax":"voter_json/",	
		"deferRender": true,
	});

	// Apply the search
    table.columns().every( function () {
        var that = this;
 
        $( 'input', this.footer() ).on( 'keydown', function (ev) {
            if (ev.keyCode == 13) { //only on enter keypress (code 13)
                that
                    .search( this.value )
                    .draw();
            }
        } );
    } );

    $('#party').on( 'keyup', function () {
    table
        .columns( 10 )
        .search( this.value )
        .draw();
} );


});


// $(document).ready(function() {
//     // Setup - add a text input to each footer cell
//     $('#example tfoot th').each( function () {
//         var title = $(this).text();
//         $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
//     } );
 
//     // DataTable
//     var table = $('#example').DataTable();
 
    // // Apply the search
    // table.columns().every( function () {
    //     var that = this;
 
    //     $( 'input', this.footer() ).on( 'keyup change', function () {
    //         if ( that.search() !== this.value ) {
    //             that
    //                 .search( this.value )
    //                 .draw();
    //         }
    //     } );
    // } );
// } );



// $(document).ready(function() {
// 	console.log("Loaded lets go");
// 	var table = $("#voter_table").DataTable( {
// 		"processing": true,
// 		"serverSide":  true,
// 		"ajax":"voter_json/",	
// 		"deferRender": true,
// 		// "columnDefs": [
// 		// 	{
// 		// 		"render": function(data, type, row) {
// 		// 			console.log(data);
// 		// 			return "<input type='checkbox' class='signatureCheck' data-voteid='"+ row[0] +"' " + (data ? "checked" : "") + " />"; 
// 		// 		},
// 		// 		"targets": 14
// 		// 	}
// 		//]
// 	});




// 	$(document).on('change', '.signatureCheck', function(){
// 		var voteid = $(this).data("voteid");
// 		var checked =  $(this).is(":checked");
// 		console.log(checked);
// 		$.post("voter_signature/", {"voteID": voteid, "checked": checked, "csrfmiddlewaretoken":'{{csrf_token}}'},   function(data){
// 			console.log("updated");
// 		});
// 	});
// });
