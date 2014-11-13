(function($) {

	function supportedBrowser(browser) {
		var supported = true;
		if (browser.msie && parseFloat(browser.version) < 9.0) {
			supported = false;
		} else if (browser.webkit && parseFloat(browser.version) < 530.0) {
			supported = false;
		} else if (browser.mozilla && parseFloat(browser.version) < 4) {
			supported = false;
		}
		return supported;
	}

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

		/* Warn for old browsers */
		if (!supportedBrowser($.browser) && $.cookie('ignoreBrowser') !== 'True') {
			$("#msie").lightbox_me({
				centered: true,
				onLoad: function() {
					$('#ok').click(function() {
						$.cookie('ignoreBrowser', 'True');
						$('#msie').trigger('close');
					});
				}
			});
		}
	});
})(jQuery);