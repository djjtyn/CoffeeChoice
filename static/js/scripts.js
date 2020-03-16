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


  