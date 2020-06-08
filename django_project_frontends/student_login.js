function subFunction()
{   
        var xhttp = new XMLHttpRequest();
        var url = "http://127.0.0.1:8000/users/student_login/";
        xhttp.open("POST", url, true);
        xhttp.setRequestHeader("Content-Type", "application/json");
        xhttp.setRequestHeader("Content-Type", "application/json");
        xhttp.onreadystatechange = function() {
          console.log("entered");
          xhttp.onload=function(){
          if (this.readyState == 4 && this.status == 200) {
           
          data=JSON.parse(this.response);
          
          
          if(data!="wrong credentials"){
          loc="http://localhost/files/backend_student.html?un="+data[0].USER_NAME+"";
         // alert(loc);
            window.open(loc,
            "_blank");
            }//loc should be a string 
          else{
            alert(data);
          }
          }
          }
        }
      
        
        var USER_NAME=document.getElementById("USER_NAME").value;
       
        var PASSWORD=document.getElementById("PASSWORD").value;
        
       
        var data = JSON.stringify({'USER_NAME':USER_NAME,'PASSWORD':PASSWORD});
        
        xhttp.send(data);
       alert(xhttp.readyState);
      }
         