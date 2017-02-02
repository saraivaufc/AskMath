
function resize_window() {
	var body = parseInt($("body").css("height"));
	var header = parseInt($("#header").css("height"));
	var breadcrumb = parseInt($("#breadcrumb").css("height"));
	var messages = parseInt($("#messages").css("height"));
	var content = parseInt($("#content").css("height"));
	var footer = parseInt($("#footer").css("height"));
	$("#content").css({"min-height":(body - header - breadcrumb - messages - footer) + "px"});
}

$(function(){
	resize_window();
	$(window).resize(resize_window);
})


Notification.requestPermission(function(perm) {
	if (perm === "granted") {
		send_alerts();
	}
});

function send_alerts(){
	$(".alert").each(function(){
		$(this).css({'display': 'none'});
		$(this).find('.message').each(function(){
			var notification = new Notification($(this).data('tag'), {
				icon: "icon.png",
				body: $(this).text()
			});
		});
	});
}

$('[data-toggle="tooltip"]').tooltip();

function create_objects(fields){
	for(var i=0; i < fields.length; i++){
		var field = $(fields[i].id);
		create_object(field, fields[i].url);			
	}
}

function create_object(element, url){
	var i = $("<i>").addClass("fa fa-plus");
	var button = $("<a>").addClass("btn btn-success btn-sm text-white").attr("type", "cancel").append(i);
	console.log(button);
	var button_plus=$(element).parent().parent().find('.btn-plus').append(button);
	button.on('click', function(){
		var url_ = window.location.origin + url;
		create_window(element, url_);
	});
}


function create_window(element, url){
	newWindow= window.open(url+"?is_popup=true", "sds",'height=500,width=800,resizable,scrollbars,dependent');
	newWindow.focus();
	newWindow.addEventListener('load', function(){
		var form = $(newWindow.document.forms[0]);
		$(form).on('submit', function(event){
			event.preventDefault();
			submit_form(element, form, url);
		});
	});
}

function submit_form(element, form, url){
	$.post(url, $(form).serialize()).done(function(data){
		if(data.status === 'success'){
			var option = $("<option>", {
				"value": data.pk,
				"selected": true,
				"text" : data.representation,
			});
			element.append(option);
			newWindow.close();
			newWindow=null;
		}else if(data.status === 'error'){
			$('input, select, textarea',$(form) ).each(function(){
				var error = data.errors[$(this).attr('name')];
				if(error){
					var li = $("<li>").text(error);
					var ul = $("<ul>").addClass("errorlist").append(li);
					$(this).parent().find("ul.errorlist").remove();
					$(this).parent().append(ul);
				}
			});
		}
	}).fail(function(data){
		alert(data.statusText);
	});
}