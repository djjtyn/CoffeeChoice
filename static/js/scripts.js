function initMap() {
    var location = {lat: 53.458479,lng: -6.219895};
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: location
    });
    var marker = new google.maps.Marker({
    position: location,
    map: map,
    title: 'Our Location'
  });
}

//Invokes the show function as soon as the page is loaded
$( document ).ready(function() {
    show();
});


var index = 0;

function show(){
    var i;
    var slides = document.getElementsByClassName("slide")
    for (i=0; i<slides.length; i++){
        slides[i].style.display = "none";
    }
    index = index + 1;
    if(index>slides.length) {
        index = 1;
    }
    slides[index-1].style.display = "block";
    setTimeout(show,3500);
}

  