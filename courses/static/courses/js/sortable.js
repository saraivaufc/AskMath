$(document).ready(function() {
	function update(){
		$("fieldset.module > table > tbody > tr > td.field-position input").each(function(index){
			index++;
			$(this).val(index);
		});
	}

	$("fieldset.module > table > tbody").sortable({
		itemSelector: "tr",
		onDrop: function($item, container, _super, event){
			update();
		},
	}).change(function(){
		update();
	});
});