Title: Wilkommen
Lang: de
Date: 2012-12-31 08:25
Tags: Welcome
Category: General
Slug: wilkommen
Author: Ross Crawford-d'Heureuse

_Private Sale Villa (owner seller)_

<div id="map_canvas" style="width:512px;height:480px"></div>

Das im Sommer 1995 fertiggestellte Anwesen einer Architekten-Familie liegt im Landschaftsschutzgebiet "Hardter Wald" von Mönchengladbach, in Nachbarschaft zu weiteren bis zu 15.000 qm großen Grundstücken.

Mönchengladbach-Hardt verfügt über eine vollständige Infrastruktur mit hohem Freizeitwert und ausgezeichneten Verkehrsanbindungen über Autobahnen zu den Städten Düsseldorf, Köln, Krefeld und Roermond.

Das von einem Landschaftsarchitekten geplante und parkähnlich angelegte Grundstück mit altem Baumbestand ist nahezu uneinsehbar. Die Bewässerung der Außenanlagen und Teiche erfolgt über Grundwasser mit eigenem Brunnenrecht.

![Exterior view](/static/images/garden-3.jpg "View from Entrance")

Die auch nachträglich variable Grundrissgestaltung mit Raumhöhen zwischen 2,75m (im Obergeschoss) und 3,60m (Erdgeschoss) wird durch eine Ausbaureserve des Dachraumes mit großflächig ausreichender Kopfhöhe ergänzt.

![Interior Dining](/static/images/interior-dining.jpg "View from Dining Room")

Eine umlaufend begehbare Dachterrasse sowie die Vorkehrung für einen offenen Kamin im Erdgeschoss bieten weitere Gestaltungsmöglichkeiten.

Raumhohe zweifarbige Alu-Fensteranlagen und polygonale Naturschieferböden im Erdgeschoss, Laminat im Obergeschoss, betonen die großzügige und lichtdurchflutete Grundrissgestaltung.

![Exterior view](/static/images/teich-1.jpg "View from First Floor")

Zwei große Terrassen im Süden und Westen des Hauses sind ebenfalls mit Naturschiefer belegt und bewirken damit den fließenden Übergang in die umgebende Natur, die von jedem Raum aus allgegenwärtig ist.

![Interior Stairs](/static/images/interior-stair.jpg "Interior Stairs")

Die vielfältigen Details der Einbauten (Türen / Waschtische / Treppenanlage etc.) weisen ein hohes Maß an Individualität jenseits jeder Alltäglichkeit auf, da es sich um Einzelanfertigungen handelt.

## Laut ENEV-Nachweis (2008): „11 Liter Haus“ ##
 

# Objektdaten #

<table>
<tr><td>Keller</td><td> ca.</td><td>27 qm</td></tr>
<tr><td>Erdgeschoss</td><td>ca.</td><td>252 qm</td></tr>
<tr><td>Obergeschoss</td><td>ca.</td><td>86 qm</td></tr>
<tr><td>Dachraum</td><td>ca.</td><td>36 qm</td></tr>
</table>

**Fußbodenheizung (Flüssiggas)**


![The Villa in the forest](/static/images/welcome.jpg "The Villa in the forest")

# Kaufpreis #

<table>
<tr>
<td>** € (Euro) **</td><td>1,950,000</td>
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
