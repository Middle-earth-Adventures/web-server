$(function() {
	$("#acc_signin_b").on("click", function() {
		console.log("logging in");
		postSignin();
	});
})

var postSignin = function() {
	jsonData = {
		"user": $("#user_i").val(),
		"password": $("#pass_i").val(),
	};
	console.log(jsonData);

	ajaxSetup();
	$.ajax({
	    type : "POST",
	    url : "/accounts/signin",
	    data : JSON.stringify(jsonData),
	    headers: {
	      'Accept': 'application/json',
	      'Content-Type': 'application/json'
	    },
	    success: function() {},
	    error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("status: " + textStatus);
			console.log("data: " + XMLHttpRequest.responseText);
			console.log("error: " + errorThrown);
			showErrorAtSignin();
	    }
	});
}

var postSignout = function() {
	ajaxSetup();
	$.ajax({
	    type : "POST",
	    url : "/accounts/signout",
	    data : JSON.stringify(jsonData),
	    headers: {
	      'Accept': 'application/json',
	      'Content-Type': 'application/json'
	    },
	    success: function() {},
	    error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("status: " + textStatus);
			console.log("data: " + XMLHttpRequest.responseText);
			console.log("error: " + errorThrown);
			showErrorAtSignin();
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

