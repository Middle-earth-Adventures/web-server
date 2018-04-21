/** WINDOW LOADED ********************/
$(function() {
	// Attack event to form buttons
	$("#acc_signup_switch_b").on("click", function() {
		console.log("switch looks");
		formLooksSwitch();
	});
	$("#acc_signup_b").on("click", function() {
		console.log("create account pressed");
		postAccountCreation();
	});
	$("#accform_to_signin_b").on("click", function() {
		console.log("switch looks back to signin");
		formLooksSwitch();
	});
});


/** FORM LOOKS SWITCH ****************/

var formLooksSwitch = function() {
	$("#email_l_c").toggleClass("dontShow");
	$("#email_i_c").toggleClass("dontShow");
	$("#acc_signup_switch_b").toggleClass("dontShow");
	$("#acc_signup_b").toggleClass("dontShow");
	$("#acc_signin_b").toggleClass("dontShow");
	$("#accform_to_signin_b_c").toggleClass("dontShow");
	$("#error_signupmsg_c").addClass("dontShow");
	$("#success_signupmsg_c").addClass("dontShow");
	$("#error_signinmsg_c").addClass("dontShow");
}

/** POST FOR ACCOUNT CREATION ********/

var postAccountCreation = function() {
	jsonData = {
		"email" : $("#email_i").val(),
		"user": $("#user_i").val(),
		"password": $("#pass_i").val(),
	};
	console.log(jsonData);

	ajaxSetup();
	$.ajax({
	    type : "POST",
	    url : "/accounts/create",
	    data : JSON.stringify(jsonData),
	    headers: {
	      'Accept': 'application/json',
	      'Content-Type': 'application/json'
	    },
	    success: function(data, textStatus, jqXHR){
	        formLooksSwitch();
	        showSuccessAtAccCreation();
	    },
	    error: function(XMLHttpRequest, textStatus, errorThrown) {
			console.log("status: " + textStatus);
			console.log("data: " + XMLHttpRequest.responseText);
			console.log("error: " + errorThrown);
			showErrorAtAccCreation();
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

var showErrorAtAccCreation = function() {
	//$("#error_msg_c").toggleClass("dontShow") // cambiar por seteo y no toggle
	$("#error_signupmsg_c").removeClass("dontShow");
	$("#success_signupmsg_c").addClass("dontShow")
	if (!$("#error_signinmsg_c").hasClass("dontShow")) $("#error_signinmsg_c").addClass("dontShow");
}
var showSuccessAtAccCreation = function() {
	//$("#success_msg_c").toggleClass("dontShow") // cambiar por seteo y no toggle
	$("#success_signupmsg_c").removeClass("dontShow");
	$("#error_signupmsg_c").addClass("dontShow")
	if (!$("#error_signinmsg_c").hasClass("dontShow")) $("#error_signinmsg_c").addClass("dontShow");
}
var showErrorAtSignin = function() {
	//$("#error_msg_c").toggleClass("dontShow") // cambiar por seteo y no toggle
	$("#error_signinmsg_c").removeClass("dontShow");
	$("#error_signupmsg_c").addClass("dontShow");
}

