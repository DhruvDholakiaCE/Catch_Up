var myInput = document.getElementById("newpswd");
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
	var vp = document.getElementById("newpswd").value;
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
	
	var un = document.getElementById("usr").value;
	var newp = document.getElementById("newpswd").value;
	var cp = document.getElementById("confirmpswd").value;
	
	var small = /[a-z]/.test(newp);
	var capital = /[A-Z]/.test(newp);
	var num = /[0-9]/.test(newp);

	if (newp.length < 8){
		alert("Password must contain at least 8 characters");
		document.getElementById("newpswd").focus();
		document.getElementById("newpswd").select();
		return false;
	}
	
	else if (!(small && capital && num)){
		alert("Please fill all the details of Password");
		document.getElementById("newpswd").focus();
		document.getElementById("newpswd").select();
		return false;
	}
	
	else if(newp!=cp){
		document.getElementById("confirmpswd").focus();
		document.getElementById("confirmpswd").select();
		return false;
	}
	
	else{
		return true;
	}
}
function resetfun(){
	document.getElementById("usr").focus();
	
	letter.classList.remove("valid");
    letter.classList.add("invalid");
	
	capital.classList.remove("valid");
    capital.classList.add("invalid");
	
	number.classList.remove("valid");
    number.classList.add("invalid");
	
	length.classList.remove("valid");
    length.classList.add("invalid");
}
