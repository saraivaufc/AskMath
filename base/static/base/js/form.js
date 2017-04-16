
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