// Creating map object  
var myMap = L.map("map", {
  center: [34.025874, -118.360857],
  zoom: 11
});

// Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Assign variable for data source (e.g. assemble via API query URL)
var locations_data = "data/locations.csv"
console.log(locations_data)

var scoring_data = "data/scoring.csv"
console.log(scoring_data)

// Grab the locations data via d3.csv
d3.csv(locations_data, 
  function(locationsRes)
  {
    console.log(locationsRes[1])
    // Grab the scoring data via d3.csv
    d3.csv(scoring_data,
    function(scoringRes)
    {
    console.log(scoringRes[39])

// Create a new marker cluster group
var markers = new L.MarkerClusterGroup({
  maxClusterRadius: 120,
  singleMarkerMode: false,
  spiderfyDistanceMultiplier: 5
});

// Loop through data
for (var i = 0; i < locationsRes.length; i++) {

    // Create a new facility object with properties of both Response objects
    var restaurant = Object.assign({},locationsRes[i],scoringRes[i]);

    // Set the data latitude and longtitude
    var lat = restaurant.lat;
    var lng = restaurant.lng;
    if(i < restaurant.length/50){
        console.log(typeof lat);
        console.log(lat);
        console.log(restaurant[0]);
    }

    // Check for lat, lng service request property
    if (lat) {
        if (lng) {

    var scoreIcon;

    if (restaurant.score > 89) {
      scoreIcon = "letterA";
    }
    else if (restaurant.score > 79) {
      scoreIcon = "letterB";
    }
    else {
      scoreIcon = "letterC";
    }

  var icons = {
    letterA: new L.icon({
      iconUrl: 'https://jmc39.github.io/img/letterA.png',
      iconSize: [39, 39],
      iconAnchor: [22, 39],
      popupAnchor: [-3, -76]
    }),
    letterB: new L.icon({
      iconUrl: 'https://jmc39.github.io/img/letterB.png',
      iconSize: [39, 39],
      iconAnchor: [22, 39],
      popupAnchor: [-3, -76]
    }),
    letterC: new L.icon({
      iconUrl: 'https://jmc39.github.io/img/letterC.png',
      iconSize: [39, 39],
      iconAnchor: [22, 39],
      popupAnchor: [-3, -76]
    }),
  };
    // Add a new marker to the cluster group and bind a pop-up
    markers.addLayer(L.marker([lat, lng], {icon: icons[scoreIcon]})
    .bindPopup(	
        `Grade: ${restaurant.grade} Scoring: ${restaurant.score}<br>
        Facility ID: ${restaurant.facility_id}<br>
        Address: ${restaurant.facility_address}<br>
        ${restaurant.facility_city}, ${restaurant.facility_state} 
        ${restaurant.facility_zip}<br>
        `));
        }   
    }
}
  // Add our marker cluster layer to the map
  myMap.addLayer(markers);
});
});