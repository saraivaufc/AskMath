$(function(){
	$("button#next").on('click', function(){
		setTimeout(function() {
			$("#introduction").hide();
		}, 500);
		$("#introduction").css({'-webkit-animation-name':'slide_out'});
		$("#question").show();
	});
});

/*

function loadSearch(){
	var data = [];
	var search = $("input[name='search']");
	var url = Urls['ask:api_course']() + "?format=json"; 
	$.get(url, function(objects){
		for(var i=0; i<objects.length; i++){
			var object = {id: objects[i].slug, text:objects[i].name}
			data.push(object);
		}
		search.select2({
		  data: data
		});
	});
	url = Urls['ask:api_lesson']() + "?format=json"; 
	$.get(url, function(objects){
		for(var i=0; i<objects.length; i++){
			var object = {id: objects[i].slug, text:objects[i].name}
			data.push(object);
		}
		search.select2({
		  data: data
		});
	});

}

$(function(){
	loadSearch();	
})

*/