function checkEmail(){
    var email = document.getElementById("email").innerHTML;
    var pattern = /@/i;
    var pos = email.search(pattern);
    if(pos == 6){
        document.getElementById("email").style.borderColor = "red";
    }
}
