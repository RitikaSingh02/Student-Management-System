    function submitfun(USER_NAME){

      alert('DO YOU WANNA DELETE THE SELECTED STUDENT');
                
      var request = new XMLHttpRequest();
      var url = "http://127.0.0.1:8000/users/delete/";
      request.open("POST", url, true);
      request.setRequestHeader("Content-Type", "application/json");
      request.onreadystatechange = function () {
        location.reload();

      };
    

     


      var data = JSON.stringify({'USER_NAME':USER_NAME});
      console.log(typeof data);
     
      request.send(data);

  };

