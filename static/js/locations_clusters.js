// Creating map object
  
var myMap = L.map("map", {
  center: [33.7701, -118.1937],
  zoom: 9
});
// function createMap(serviceRequests) {

// Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Assign variable for data source (e.g. assemble via API query URL)
var file = "static/js/locations.csv"
console.log(file)

// Grab the data with d3
d3.csv(file, 
  function(response) {
  console.log(response);

// Create a new marker cluster group
var markers = L.markerClusterGroup();

// Loop through data
for (var i = 0; i < response.length; i++) {
    console.log(response[i].lat)

    // Set the data latitude and longtitude
    var lat = response[i].lat;
    var lng = response[i].lng;
    // if(i < response.length/50){
    //     console.log(typeof lat);
    //     console.log(lat);
    //     console.log(response[0]);
    // }

    // Check for lat, lng service request property
    if (lat) {
        if (lng) {
    // Add a new marker to the cluster group and bind a pop-up
    markers.addLayer(L.marker([lat, lng])
    .bindPopup(	
        `Facility ID: ${response[i].facility_id}<br>
        Address: ${response[i].facility_address}<br>
        ${response[i].facility_city}, ${response[i].facility_state} ${response[i].facility_zip}<br>
        `));
        }   
    }
}
  // Add our marker cluster layer to the map
  myMap.addLayer(markers);
});