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

		/* Warn for IE */
		if ($.browser.msie) {
			$("#msie").lightbox_me({
				centered: true,
				onLoad: function() {
					$('#ok').click(function() {
						$('#msie').trigger('close');
					})
				}
			});
		}
	});
})(jQuery);