function submitfun(){
  var c=1;
  var request = new XMLHttpRequest();
  var url = "http://127.0.0.1:8000/users/insert/";
  request.open("POST", url, true);
  request.setRequestHeader("Content-Type", "application/json");
  request.onreadystatechange = function () {
      console.log("yes");
      
      if (request.readyState === 4 && request.status === 200) {
        c=0;
        var json = JSON.parse(request.response);
        alert(json);

  }

};
  var USER_NAME=document.getElementById("USER_NAME").value;
  var father_name = document.getElementById("father_name").value;
  var email = document.getElementById("email").value;
  var branch = document.getElementById("branch").value;
  var phone_no = document.getElementById("phone_no").value;
if(c==0){
    alert("student not inserted check for duplicate entries");
}
else{
    alert("student inserted successfully");
}
  var data = JSON.stringify({"USER_NAME":USER_NAME ,"father_name": father_name, "email": email, "branch": branch, "phone_no": phone_no});
  request.send(data);

};

