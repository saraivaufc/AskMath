function active_constrast(){
	$("body").addClass("highcontrast");	
	
	var button_contrast = $("#button-contrast");
	button_contrast.removeClass("disable-contrast");
	button_contrast.addClass("enable-contrast");
	button_contrast.text("Alto Contraste-ON [3]");
}

function disable_constrast(){
	$("body").removeClass("highcontrast");	

	var button_contrast = $("#button-contrast");
	button_contrast.removeClass("enable-contrast");
	button_contrast.addClass("disable-contrast");
	button_contrast.text("Alto Contraste-OFF [3]");
}

function set_font(size){
	$("h1, h2, h3, h4, h5, h6, p, label, a").each(function(){
		var font = parseInt($(this).css("font-size")) + parseInt(size);
		$(this).css({"font-size": font + "px" });
	});
}

function alter_font(size){
	set_font(size);
	var font = Cookies.get("font");
	if(font === undefined){
		font = size;
	}else{
		font = parseInt(font) + parseInt(size);
	}
	Cookies.set("font", font);
}


function accessibility(){
	if(Cookies.get("contrast")){
		active_constrast();
	}

	if(Cookies.get("font")){
		set_font(Cookies.get("font"));
		var button_font = $("#button-font");
		button_font.removeClass("font-minus");
		button_font.addClass("font-plus");
		button_font.text("Big Font-ON [4]");

	}
}

accessibility();

$("#button-contrast").click(function(){
	if($(this).hasClass("disable-contrast")){
		active_constrast();
		Cookies.set("contrast", true);
		console.log("Contrar Enable");
	}else if($(this).hasClass("enable-contrast")){
		disable_constrast();
		Cookies.remove("contrast");
		console.log("Contrar Disable");
	}
});

$("#increase-font").click(function(){
	alter_font(2);
});

$("#decrease-font").click(function(){
	alter_font(-2);
});
