function submitfun(){

  alert("student inserted successfully");
  var request = new XMLHttpRequest();
  var url = "http://127.0.0.1:8000/users/insert/";
  request.open("POST", url, true);
  
  request.setRequestHeader("Content-Type", "application/json");
  request.onreadystatechange = function () {
      
      
      if (request.readyState === 4 && request.status === 200) {
        console.log(this.responseText);
  }

};
  var USER_NAME=document.getElementById("USER_NAME").value;
  var father_name = document.getElementById("father_name").value;
  var email = document.getElementById("email").value;
  var branch = document.getElementById("branch").value;
  var phone_no = document.getElementById("phone_no").value;

  var data = JSON.stringify({"USER_NAME":USER_NAME ,"father_name": father_name, "email": email, "branch": branch, "phone_no": phone_no});
 
  request.send(data);

};

