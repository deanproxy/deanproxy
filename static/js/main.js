(function($) {
	$(document).ready(function() {
		$('input[name=query]').focus(function() {
			if ($(this).val() === 'Search') {
				$(this).val('');
			}
		}).blur(function() {
			if ($(this).val() === '') {
				$(this).val('Search');
			}
		});
	});
})(jQuery);