var sel1 = document.querySelector('#main_select');
var sel2 = document.querySelector('#child_select');
var options2 = sel2.querySelectorAll('option');

function giveSelection(selValue) {
  sel2.innerHTML = '';
  for(var i = 0; i < options2.length; i++) {
    if(options2[i].dataset.option === selValue) {
      sel2.appendChild(options2[i]);
    }
  }
}

giveSelection(sel1.value);