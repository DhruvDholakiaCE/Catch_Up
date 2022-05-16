var myInput = document.getElementById("pswd");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {  
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }
  
  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {  
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }
  
  // Validate length
  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}

function confirmvalidation() {
	var vp = document.getElementById("pswd").value;
	var vcp = document.getElementById("confirmpswd").value;
	if (vcp!=vp){
		document.getElementById("cmsg").style.display="inline-block";
		document.getElementById("confirmpswd").style.color="red";
	}
	else{
		document.getElementById("cmsg").style.display="none";
		document.getElementById("confirmpswd").style.color="black";
	}
}

function validateForm() {
	
	var firstname = document.forms["signup"]["firstname"].value;
	var lastname = document.forms["signup"]["lastname"].value;
	var newp = document.forms["signup"]["pswd"].value;
	var cp = document.forms["signup"]["confirmpswd"].value;
	
	var small = /[a-z]/.test(newp);
	var capital = /[A-Z]/.test(newp);
	var num = /[0-9]/.test(newp);
	
	if (firstname.length > 32)
	{
		alert("FirstName should be no greater than 32 characters");
		document.forms["signup"]["firstname"].focus();
		document.forms["signup"]["firstname"].select();
		return false;
	}
	
	else if (lastname.length > 32)
	{
		alert("LastName should be no greater than 32 characters");
		document.forms["signup"]["lastname"].focus();
		document.forms["signup"]["lastname"].select();
		return false;
	}

	else if (newp.length < 8){
		alert("Password must contain at least 8 characters");
		document.forms["signup"]["pswd"].focus();
		document.forms["signup"]["pswd"].select();
		return false;
	}
	
	else if (!(small && capital && num)){
		alert("Please fill all the details of Password");
		document.forms["signup"]["pswd"].focus();
		document.forms["signup"]["pswd"].select();
		return false;
	}
	
	else if(newp!=cp){
		document.forms["signup"]["confirmpswd"].focus();
		document.forms["signup"]["confirmpswd"].select();
		return false;
	}
	
	else{
		return true;
	}
}
function resetfun(){
	document.getElementById("firstname").focus();
	
	letter.classList.remove("valid");
    letter.classList.add("invalid");
	
	capital.classList.remove("valid");
    capital.classList.add("invalid");
	
	number.classList.remove("valid");
    number.classList.add("invalid");
	
	length.classList.remove("valid");
    length.classList.add("invalid");
}
