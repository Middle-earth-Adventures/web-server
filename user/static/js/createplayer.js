$(function() {
	$("#player_create_b").on("click", function() {
		postCreatePlayer();
	});
	$("#acc_logout_b").on("click", function() {
		postSignout();
	});
})

var postCreatePlayer = function() {
	jsonData = {
		"name" : $("#name_i").val(),
	};

	ajaxSetup();
	$.ajax({
	    type : "POST",
	    url : "/player/create",
	    data : JSON.stringify(jsonData),
	    success: function(data, textStatus, jqXHR){
	        blankCreatePlayerForm();

	        //refresh player's list
	        postCreatePlayersList();
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

var blankCreatePlayerForm = function() {
	$("#name_i").val("")
}
var showSuccessAtPlayerCreation = function() {
	$("#success_playermsg_c").removeClass("dontShow");
	$("#error_playermsg_c").addClass("dontShow");
}

var showErrorAtPlayerCreation = function() {
	$("#error_playermsg_c").removeClass("dontShow");
	$("#success_playermsg_c").addClass("dontShow");
}
