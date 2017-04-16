
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

$('[data-toggle="tooltip"]').tooltip();

$("select[name='language']").change(function(){
	$(this).parent().submit();
});