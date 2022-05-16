var btnpi = document.getElementById("btnpi");
var btnedu = document.getElementById("btnedu");
var btnexp = document.getElementById("btnexp");
var btnskills = document.getElementById("btnskills");
var btnla = document.getElementById("btnla");

var divpi = document.getElementById("divpi");
var divedu = document.getElementById("divedu");
var divexp = document.getElementById("divexp");
var divskills = document.getElementById("divskills");
var divla = document.getElementById("divla");

btnpi.addEventListener("mouseover", mouseOverpi);
btnpi.addEventListener("mouseout", mouseOutpi);

btnedu.addEventListener("mouseover", mouseOveredu);
btnedu.addEventListener("mouseout", mouseOutedu);

btnexp.addEventListener("mouseover", mouseOverexp);
btnexp.addEventListener("mouseout", mouseOutexp);

btnskills.addEventListener("mouseover", mouseOverskills);
btnskills.addEventListener("mouseout", mouseOutskills);

btnla.addEventListener("mouseover", mouseOverla);
btnla.addEventListener("mouseout", mouseOutla);

function mouseOverpi(event){
	btnpi.style.backgroundColor = "#fdd54f";
	btnpi.style.color="#000";
}
function mouseOutpi(event){
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
}

function mouseOveredu(event){
	btnedu.style.backgroundColor = "#fdd54f";
	btnedu.style.color="#000";
}
function mouseOutedu(event){
	btnedu.style.backgroundColor = "#000";
	btnedu.style.color="#fdd54f";
}

function mouseOverexp(event){
	btnexp.style.backgroundColor = "#fdd54f";
	btnexp.style.color="#000";
}
function mouseOutexp(event){
	btnexp.style.backgroundColor = "#000";
	btnexp.style.color="#fdd54f";
}

function mouseOverskills(event){
	btnskills.style.backgroundColor = "#fdd54f";
	btnskills.style.color="#000";
}
function mouseOutskills(event){
	btnskills.style.backgroundColor = "#000";
	btnskills.style.color="#fdd54f";
}

function mouseOverla(event){
	btnla.style.backgroundColor = "#fdd54f";
	btnla.style.color="#000";
}
function mouseOutla(event){
	btnla.style.backgroundColor = "#000";
	btnla.style.color="#fdd54f";
}

divedu.style.display = "none";
divexp.style.display = "none";
divskills.style.display = "none";
divla.style.display = "none";
divpi.style.display = "block";

if (divpi.style.display == "block"){
	btnpi.style.color = "#000";
	btnpi.style.backgroundColor = "#fdd54f";
}

function openPI(){
	btnpi.style.backgroundColor = "#fdd54f";
	btnpi.style.color="#000";
	btnpi.removeEventListener("mouseout", mouseOutpi);
	
	btnedu.style.backgroundColor = "#000";
	btnedu.style.color="#fdd54f";
	btnedu.addEventListener("mouseout", mouseOutedu);
	
	btnexp.style.backgroundColor = "#000";
	btnexp.style.color="#fdd54f";
	btnexp.addEventListener("mouseout", mouseOutexp);
	
	btnskills.style.backgroundColor = "#000";
	btnskills.style.color="#fdd54f";
	btnskills.addEventListener("mouseout", mouseOutskills);
	
	btnla.style.backgroundColor = "#000";
	btnla.style.color="#fdd54f";
	btnla.addEventListener("mouseout", mouseOutla);
	
	divpi.style.display = "block";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}
function openEdu(){
	btnedu.style.backgroundColor = "#fdd54f";
	btnedu.style.color="#000";
	btnedu.removeEventListener("mouseout", mouseOutedu);
	
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", mouseOutpi);
	
	btnexp.style.backgroundColor = "#000";
	btnexp.style.color="#fdd54f";
	btnexp.addEventListener("mouseout", mouseOutexp);
	
	btnskills.style.backgroundColor = "#000";
	btnskills.style.color="#fdd54f";
	btnskills.addEventListener("mouseout", mouseOutskills);
	
	btnla.style.backgroundColor = "#000";
	btnla.style.color="#fdd54f";
	btnla.addEventListener("mouseout", mouseOutla);
	
	divedu.style.display = "block";
	divpi.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openExp(){
	btnexp.style.backgroundColor = "#fdd54f";
	btnexp.style.color="#000";
	btnexp.removeEventListener("mouseout", mouseOutexp);
	
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", mouseOutpi);
	
	btnedu.style.backgroundColor = "#000";
	btnedu.style.color="#fdd54f";
	btnedu.addEventListener("mouseout", mouseOutedu);
	
	btnskills.style.backgroundColor = "#000";
	btnskills.style.color="#fdd54f";
	btnskills.addEventListener("mouseout", mouseOutskills);
	
	btnla.style.backgroundColor = "#000";
	btnla.style.color="#fdd54f";
	btnla.addEventListener("mouseout", mouseOutla);
	
	divexp.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divskills.style.display = "none";
	divla.style.display = "none";
}

function openSkills(){
	btnskills.style.backgroundColor = "#fdd54f";
	btnskills.style.color="#000";
	btnskills.removeEventListener("mouseout", mouseOutskills);
	
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", mouseOutpi);
	
	btnedu.style.backgroundColor = "#000";
	btnedu.style.color="#fdd54f";
	btnedu.addEventListener("mouseout", mouseOutedu);
	
	btnexp.style.backgroundColor = "#000";
	btnexp.style.color="#fdd54f";
	btnexp.addEventListener("mouseout", mouseOutexp);
	
	btnla.style.backgroundColor = "#000";
	btnla.style.color="#fdd54f";
	btnla.addEventListener("mouseout", mouseOutla);
	
	divskills.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divla.style.display = "none";
}

function openLA(){
	btnla.style.backgroundColor = "#fdd54f";
	btnla.style.color="#000";
	btnla.removeEventListener("mouseout", mouseOutla);
	
	btnpi.style.backgroundColor = "#000";
	btnpi.style.color="#fdd54f";
	btnpi.addEventListener("mouseout", mouseOutpi);
	
	btnedu.style.backgroundColor = "#000";
	btnedu.style.color="#fdd54f";
	btnedu.addEventListener("mouseout", mouseOutedu);
	
	btnexp.style.backgroundColor = "#000";
	btnexp.style.color="#fdd54f";
	btnexp.addEventListener("mouseout", mouseOutexp);
	
	btnskills.style.backgroundColor = "#000";
	btnskills.style.color="#fdd54f";
	btnskills.addEventListener("mouseout", mouseOutskills);
	
	divla.style.display = "block";
	divpi.style.display = "none";
	divedu.style.display = "none";
	divexp.style.display = "none";
	divskills.style.display = "none";
}
