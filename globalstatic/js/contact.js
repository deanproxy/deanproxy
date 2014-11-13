(function($) {

	$.validator.addMethod('isEmpty', function(value, element) {
		return this.optional(element) || value !== 'someone@something.com';
	}, 'Please enter a valid email address.');

	$(document).ready(function() {
		$('#email').focus(function() {
			if ($(this).val() === 'someone@something.com') {
				$(this).val('');
			}
		}).blur(function() {
			if ($(this).val() === '') {
				$(this).val('someone@something.com');
			}
		});

		$('#clear').click(function() {
			$('#message').val('');
			$('#email').val('');
			return false;
		});

		$('form[name=contact]').validate({
			wrapper: 'span',
			errorPlacement: function(error, element) {
				if (element.attr('name') != 'message') {
					error.appendTo(element.parent('li'));
				}
			},
			highlight: function(element, errorClass) {
				$(element).parent('li').addClass(errorClass);
			},
			unhighlight: function(element, errorClass){
				$(element).parent('li').removeClass(errorClass);
			}
		});
	});

})(jQuery);