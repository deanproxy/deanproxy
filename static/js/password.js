(function($) {

	$(document).ready(function() {
		$('form[name=reset]').validate({
			submitHandler: function(form) {
				var li = $('#submit').hide().parent('li');
				li.prepend('<span>Changing password <img src="/static/images/loading-pacman.gif"/></span>');
				$.post(form.action, $(form).serialize(), function() {
					li.find('span').html('Success!').addClass('success');
					window.location.href = '/blog/posts/';
				}).error(function() {
					li.find('span').html('Failed.').addClass('error');
					$('#submit').show();
				});
				return false;
			},
			rules: {
			    password: {
					required: true
				},
				password_confirm: {
					required: true,
					equalTo: '#password'
				}
			},
			errorPlacement: function() {},
			highlight: function(element, errorClass) {
				$(element).parent('li').addClass(errorClass);
			},
			unhighlight: function(element, errorClass) {
				$(element).parent('li').removeClass(errorClass);
			}
		})
	});
})(jQuery);