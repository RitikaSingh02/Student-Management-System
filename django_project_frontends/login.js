$(document).ready(function() {

    $('#myform').submit(function() {

        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:8000/users/',
             
        
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
        	async: false,
            data: JSON.stringify({
                USER_NAME: $("#USER_NAME").val(),
                PASSWORD: $("#PASSWORD").val(),
                USERTYPE: $("#USERTYPE").val()
            }),
            
         
            success: function(data)
            {
            console.log(data);
          
                if(data=="wrong credentials")
                {alert(data);
                console.log(data);}
                else{
            if(data.USERTYPE=='S'){	
            
            window.location.href = "http://localhost/files/backend_student.html"    }
            else
            {
                if(data.USERTYPE=='T')
                window.location.href = "http://localhost/files/backend_faculty.html"    
                console.log(data['USER_NAME']);
            }
        }
            }
            
        });
        //this is mandatory other wise your from will be submitted.
        return false; 
    });

});