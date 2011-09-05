(function($) {
	$(document).ready(function() {
		$('form[name=login]').validate({
			submitHandler: function(form) {
				$('#submit').hide();
				var span = $('#submit').parent('li').find('span');
				if (span.length == 0) {
					$('#submit').parent('li').prepend('<span></span>');
					span = $('#submit').parent('li').find('span');
				}
				span.html('Authenticating...').removeClass('error');
				$.post('/admin/login/', $(form).serialize(), function() {
					span.html('Success! Logging you in...').addClass('success');
					window.location.href = '/blog/posts/';
				}).error(function() {
					span.html('Failed. Try again.').addClass('error');
					$('#submit').show();
				});
				return false;
			},
			errorPlacement: function() {
				/* No where! */
			},
			highlight: function(element, errorClass) {
				$(element).parent('li').addClass(errorClass);
			},
			unhighlight: function(element, errorClass) {
				$(element).parent('li').removeClass(errorClass);
			}
		});
	});
})(jQuery);