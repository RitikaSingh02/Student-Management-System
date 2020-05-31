$(document).ready(function() {

        $('#updateform').submit(function() {
    
            $.ajax({
                type: "POST",
                url: 'http://127.0.0.1:8000/users/update/',
                 
            
                contentType: 'application/json; charset=utf-8',
                dataType: 'json',
                async: false,
                data: JSON.stringify({
                    USER_NAME: $("#USER_NAME").val(),
                    father_name: $("#father_name").val(),
                    email: $("#email").val(),
                    branch: $("#branch").val(),
                    phone_no: $("#phone_no").val(),

                }),
                
             
                success: function(data)
                {
                alert(data);
              
                    
                },
                error:function(){
                    alert("an error occured");
                }
                
            });
            //this is mandatory other wise your from will be submitted.
            return false; 
        });
    
    });
