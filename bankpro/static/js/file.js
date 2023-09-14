function hide_el (elements) {
  for(var i = 0; i < elements.length; i++)
    elements[i].style.display = 'none';
}
window.onload = function () {
  var a = document.getElementsByName('continent')[0];
  var b = document.getElementsByClassName('country');
  var c = document.getElementsByClassName('city');

  a.onchange = function () {
    hide_el(b); hide_el(c);
    var country = document.getElementById(this.value);
    if(!country) alert('No countries!');
    country.style.display = 'block';
  }
  for(var i=0; i<b.length; i++)
    b[i].onchange = function () {
      hide_el(c);
      var city = document.getElementById(this.value);
      if(!city) alert('There are no cities in ' + this.value);
      city.style.display = 'block';
    }
}