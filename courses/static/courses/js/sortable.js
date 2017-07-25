$(document).ready(function() {
	function update(root){
		$(root + " td.field-position input").each(function(index){
			index++;
			$(this).val(index);
		});
	}

	$(".module > table > tbody").sortable({
		itemSelector: "tr",
		onDrop: function($item, container, _super, event){
			update(".module > table > tbody");
		},
	}).change(function(){
		update(".module > table > tbody");
	});

	$(".results > table > tbody").sortable({
		itemSelector: "tr",
		onDrop: function($item, container, _super, event){
			update(".results > table > tbody");
		},
	}).change(function(){
		update(".results > table > tbody");
	});
});