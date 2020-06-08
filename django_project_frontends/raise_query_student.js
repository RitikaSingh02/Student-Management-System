function update() {
    var xhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/users/query_update/";
    request.open("POST", url, true);
    request.setRequestHeader("Content-Type", "application/json");
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       alert(this.responseText);
       
      }
      else
      {
          alert("request has not been approved yet");
      }
    

    };
    var father_name=document.getElementById("father_name").value();
    console.log(father_name);
    var email=document.getElementById("email").value();
    var phone_no=document.getElementById("phone_no").value();
    var branch=document.getElementById("branch").value();
    var data = JSON.stringify({'USER_NAME':USER_NAME,'father_name':father_name,'email':email,'branch':branch,'phone_no':phone_no});
    xhttp.send(data);
  }