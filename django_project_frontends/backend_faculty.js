$(document).ready(function() {



        $.ajax({
            type: "GET",
            url: 'http://127.0.0.1:8000/students/',
             
        
    contentType: 'application/json; charset=utf-8',
    dataType: 'json',
        	async: false,
            data: '',
            success: function(data){

                //If the REST API returned a successful response it'll be stored in data, 
                //just parse that field using jQuery and you're all set
            
                var tblSomething = '<thead> <tr> <td> USER_NAME </td> <td> PASSWORD </td> <td> USERTYPE</td> </tr> </thead> <tbody>';
            
                $.each(data, function(idx, obj){
            
                //Outer .each loop is for traversing the JSON rows
                tblSomething += '<tr>';
            
                //Inner .each loop is for traversing JSON columns
                $.each(obj, function(key, value){
                tblSomething += '<td>' + value + '</td>';
                });
                tblSomething += '</tr>';
                });
            
                tblSomething += '</tbody>';
            
                $('#tblSomething').html(tblSomething);
                },
                error: function(jqXHR, textStatus, errorThrown){
                alert('Hey, something went wrong because: ' + errorThrown);
                }
                });
            
            
            
        //this is mandatory other wise your from will be submitted.
        return false; 
    });

