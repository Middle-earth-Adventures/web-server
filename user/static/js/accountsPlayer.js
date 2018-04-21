$(function() {
	postCreatePlayersList();
});

var playersListAddToDOM = function(players) {
	// Espera arreglo de elementos de player
	// Ej: [{'name':valueX,'level':levleY,'stamina':staminaZ},{...}]
	var tableNode = playersListTableNode(players);
	$("#playersList-c").empty();
	$("#playersList-c").append($(tableNode));
}

var playersListTableNode = function(players) {
	var tdTemp= "<td></td>";

	var tableNode = $("<table class='table table-striped'></table");
	var theadNode = $("<thead></thead>");
	var trHeadNode= $("<tr></tr>");
	$(trHeadNode).append($("<th>Nombre</th>"));
	$(trHeadNode).append($("<th>Level</th>"));
	$(trHeadNode).append($("<th>Estamina</th>"));
	$(tableNode).append($(theadNode).append($(trHeadNode)));

	var tbodyNode = $("<tbody></tbody>");
	players.forEach(function(elem) {
		var trbodyNode= $("<tr></tr>");
		$(trbodyNode).append($(tdTemp).text(elem.name));
		$(trbodyNode).append($(tdTemp).text(elem.level));
		$(trbodyNode).append($(tdTemp).text(elem.stamina));
		$(tbodyNode).append($(trbodyNode));
	});
	$(tableNode).append($(tbodyNode));

	return tableNode;
}

/** AJAX FUNCTIONS **/

var postCreatePlayersList = function() {
	ajaxSetup();
	$.ajax({
	    type : "GET",
	    url : "player/accountsPlayers",
	    success: function(data, textStatus, jqXHR){
	    	console.log("player/accountsPlayers: Respuesta de servidor correcta");
	    	var dataFields = [];
	    	JSON.parse(data).forEach(function(elem){
	    		this.push(elem.fields);
	    	}, dataFields);
	        playersListAddToDOM(dataFields);
	    },
	    error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("status: " + textStatus);
			console.log("data: " + XMLHttpRequest.responseText);
			console.log("error: " + errorThrown);
			showErrorAtPlayerCreation();
			blankCreatePlayerForm();
	    }
	});
}

var ajaxSetup = function() {
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			function getCookie(name) {
			    var cookieValue = null;
			    if (document.cookie && document.cookie != '') {
			        var cookies = document.cookie.split(';');
			        for (var i = 0; i < cookies.length; i++) {
			            var cookie = jQuery.trim(cookies[i]);
			            // Does this cookie string begin with the name we want?
			            if (cookie.substring(0, name.length + 1) == (name + '=')) {
			                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
			                break;
			            }
			        }
			    }
			    return cookieValue;
			}
			if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
			    // Only send the token to relative URLs i.e. locally.
			    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	 		}
 		}
	});
}
