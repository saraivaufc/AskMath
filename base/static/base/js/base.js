$(function(){
	/*
	Waves.attach('.btn, .btn-floating', ['waves-light']);
	Waves.attach('.waves-light', ['waves-light']);
	Waves.attach('.navbar-nav a:not(.navbar-brand), .nav-icons li a, .navbar form, .nav-tabs .nav-item', ['waves-light']);
	Waves.attach('.pager li a', ['waves-light']);
	Waves.attach('.pagination .page-item .page-link', ['waves-effect']);
	Waves.init();
	*/
	
	$('[data-toggle="tooltip"]').tooltip();

	$("select[name='language']").change(function(){
		$(this).parent().submit();
	});
})