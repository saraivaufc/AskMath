$('[data-toggle="tooltip"]').tooltip();

$("select[name='language']").change(function(){
	$(this).parent().submit();
});