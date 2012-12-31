Title: Welcome
Lang: en
Date: 2012-12-31 08:25
Tags: Welcome
Category: General
Slug: welcome
Author: Ross Crawford-d'Heureuse

_Private Sale Villa (owner seller)_

The villa is the property of an Architect's family, completed in the summer of 1995 and situated in a registered conservation area known as the "Hardter Wald" found near the city of Mönchengladbach. The villa is surrounded by private residential plots with an average size of around 15,000 sqm; thus allowing for a peaceful and private lifestyle.

<div id="map_canvas" style="width:512px;height:480px"></div>

Mönchengladbach-Hardt while being a small town has a high-standard of recreation and international level sports facilities, infrastructure and shopping communities to ensure a comfortable lifestyle. This as well as excellent access to highways leading into the cities of Düsseldorf, Köln (Cologne), Krefeld and Roermond (Netherlands) ensures that you are never too far away from the excitement of a big city.

![Exterior view](/static/images/garden-3.jpg "View from Entrance")

Planned and developed as a park-like garden by a landscape architect; the grounds are deliberately surrounded by old-growth trees ensuring the the main house is almost totally hidden from the road.

The grounds and its large waterlandscape are fed via the owner's licensed access to the villa's own source of borewater.

![Exterior view](/static/images/teich-1.jpg "View from First Floor")

The house itself consists of 4 modern bedrooms alongside a vast open-plan living space with 3 toilets and 2 bathrooms easily accessible from both floors.

The first floor has a height of 2.75m, while the ground floor is 3.60m in height. The house has been designed to allow for the removal of certain walls thus enlarging the floor space of affected rooms.

The house allows for a fantastic view of the seasons change through the bi-coloured aluminium floor to ceiling windows, which provide a stunning "close to nature" feeling. This natural feeling is heightened by the addition of natural slate flooring on the ground floor and is accentuated by the strategic use of soft lights as well as floodlighting which accent the design on a grand scale.

![Interior Dining](/static/images/interior-dining.jpg "View from Dining Room")

A corner of the roof and deck have been designed to allow for the installation of an external chimney which can connect to an internal or external fireplace, as required by the season.

The house is extended by its two large terraces which cover the Southern and Western sunny sides of the house and are paved in the same slate as the ground floor. While the house is kept warm during the winter months by liquid gas powered underfloor heating.

![Interior Stairs](/static/images/interior-stair.jpg "Interior Stairs")

In addition to this each detail of the house has been personally selected and placed with a view to simple yet stylish modern living; from the door fittings and door-handles to the washing stands and central staircase. The house is bespoke and custom designed as well as being built to ensure its unique aspect keeps the individual in mind.

As per the "*German Energy Efficiency Certificate*" (ENEV 2008), the house is rated as an "**11 litre house**".


## Property Datasheet ##
<table>
<tr><td>Basement</td><td> ca.</td><td>27 sqm</td></tr>
<tr><td>Ground floor</td><td>ca.</td><td>252 sqm</td></tr>
<tr><td>First floor</td><td>ca.</td><td>86 sqm</td></tr>
<tr><td>Attic</td><td>ca.</td><td>36 sqm</td></tr>
</table>

![The Villa in the forest](/static/images/welcome.jpg "The Villa in the forest")


## Asking price ##
<table>
<tr>
<td>€ (Euro)</td><td>1,950,000</td>
</tr>
</table>


<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&key=AIzaSyBhGjmo_89lYuLL3pQAvGWAc4bhS3GVBE0&sensor=false"></script>
<script>
var map;
function initialize() {
  var mapOptions = {
    zoom: 18,
    //center: new google.maps.LatLng(-34.397, 150.644),
    mapTypeId: google.maps.MapTypeId.SATELLITE
  };

	map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
  	geocoder = new google.maps.Geocoder();
	geocoder.geocode( { 'address': 'Ungermannsweg 3, Monchengladbach NRW Germany'}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        //In this case it creates a marker, but you can get the lat and lng from the location.LatLng
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: map, 
            position: results[0].geometry.location
        });
      }
  	});
}

google.maps.event.addDomListener(window, 'load', initialize);
</script>


<link rel="stylesheet" type="text/css" href="/static/js/Elastislide/css/elastislide.css" />
<script type="text/javascript" src="/static/js/Elastislide/js/jquerypp.custom.js"></script>
<script type="text/javascript" src="/static/js/Elastislide/js/jquery.elastislide.js"></script>

<script type="text/javascript">
$(document).ready(function(){

	var gallery = $('<ul/>', {
		id: 'gallery',
		class: 'elastislide-list'
	});

	$('article').prepend(gallery)

	$.each($('img'), function(i,e){
		$(e).width(580).height(400)
		var a = $('<a>', {
			href: e.src,
			html: $('<img/>', {
				src: e.src
			})
		});

		$('#gallery').append($('<li></li>',{
			html: a
		}))
	});

	$('#gallery').elastislide( {
		minItems : 5,
		onClick: function(el, position, event) {
			event.preventDefault();
			var src = $(el.find('img')).attr('src');
			var image = $('[src="'+src+'"]');
			console.log(image)
			$.scrollTo(image)
		}
	});

});
</script>
