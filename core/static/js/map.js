 var map;
      var markers = [];
      function initMap() {
        map = new google.maps.Map(document.getElementById('map-canvas'), {
          center: {lat: 28.59642, lng: -81.2363699},
          zoom: 16
        });

        google.maps.event.addListener(map, 'idle', function(ev){
          // update the coordinates here
          var bounds = map.getBounds();
          var ne = bounds.getNorthEast(); // LatLng of the north-east corner
          var sw = bounds.getSouthWest(); // LatLng of the south-west corder
          var nw = new google.maps.LatLng(ne.lat(), sw.lng());
          var se = new google.maps.LatLng(sw.lat(), ne.lng());

          console.log(ne.lat(),
                        se.lat(),
                        ne.lng(),
                        sw.lng()
                      );
          
          var neLAT = ne.lat();
          var seLAT = se.lat();
          var neLNG = ne.lng();
          var swLNG = sw.lng();
          
        $.post("/voter/voter_map/", {"neLAT": neLAT, "seLAT": seLAT, "neLNG":neLNG, "swLNG": swLNG, "csrfmiddlewaretoken":'{{csrf_token}}'},  function(data) {
          deleteMarkers();
          data.forEach(function(obj) { 
            var contentString = obj.fields.party;
            var title = obj.fields.first_name;
            addMarker({lat: parseFloat(obj.fields.latitude), lng: parseFloat(obj.fields.longitude)}, contentString, title);
          });
        });
      });
    }

    // Adds a marker to the map and push to the array.
    function addMarker(location, contentString, title) {
      var infowindow = new google.maps.InfoWindow({
        content: contentString
      });

      var marker = new google.maps.Marker({
        position: location,
        map: map,
        title: title
      });

      marker.addListener('click', function() {
        infowindow.open(map, marker);
      });

      markers.push(marker);


    }

    // Sets the map on all markers in the array.
    function setMapOnAll(map) {
      for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
      }
    }

    // Removes the markers from the map, but keeps them in the array.
    function clearMarkers() {
      setMapOnAll(null);
    }

    // Shows any markers currently in the array.
    function showMarkers() {
      setMapOnAll(map);
    }

    // Deletes all markers in the array by removing references to them.
    function deleteMarkers() {
      clearMarkers();
      markers = [];
    }

  
      