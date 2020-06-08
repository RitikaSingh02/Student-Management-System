function subFunction(){
       
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/users/change_password/";
    request.open("POST", url, true);
    request.setRequestHeader("Content-Type", "application/json");
    request.onreadystatechange = function () {
        if (request.readyState === 4 && request.status === 200) {
            
            var json = JSON.parse(request.responseText);
            alert(json);
         
        }

    };
  

    loc=window.location.href;
    var USER_NAME=loc.split('=')[1]; 

    var PASSWORD=document.getElementById('PASSWORD').value;
    var data = JSON.stringify({'USER_NAME':USER_NAME,'PASSWORD':PASSWORD});
    console.log(typeof data);
   
    request.send(data);



};

