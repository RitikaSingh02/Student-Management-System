function subFunction()
{   
        var USER_NAME=document.getElementById("USER_NAME").value;
       
        var PASSWORD=document.getElementById("PASSWORD").value;
        var xmlhttp = new XMLHttpRequest();
        var url = "http://127.0.0.1:8000/users/teacher_login/";
        xmlhttp.open("POST", url, true);
        
        xmlhttp.setRequestHeader("Content-Type", "application/json");
        
        xmlhttp.onreadystatechange = function() { 
          // console.log("entered");
          xmlhttp.onload=function(){
          if (this.readyState == 4 && this.status == 200) {
            data=this.responseText;

            // alert(this.responseText);
            // alert(this.readyState);
           
                  if(data=="logged in"){
                    window.open( "http://localhost/files/backend_faculty.html",
                    "_blank");
                  }
                  else{
                    alert(data);
                    
                  }
    
          }

          };
          }
        
       
        var data = JSON.stringify({'USER_NAME':USER_NAME,'PASSWORD':PASSWORD});
        
        
        xmlhttp.send(data);
        alert(xmlhttp.readyState);//readystate=1
        
      }
         