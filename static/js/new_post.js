(function($) {
	$(document).ready(function() {
		$('input[name=title]').focus(function() {
			if ($(this).val() === 'Title of post') {
				$(this).val('');
			}
		}).blur(function() {
			if ($(this).val() === '') {
				$(this).val('Title of post');
			}
		});
		$('input[name=tags]').focus(function() {
			if ($(this).val() === 'Tags') {
				$(this).val('');
			}
		}).blur(function() {
			if ($(this).val() === '') {
				$(this).val('Tags');
			}
		});

		$('#delete').click(function() {
			var submit = false;
			if (confirm('Really delete this post?')) {
				$('form').attr('action', '/blog/posts/delete/' + $('#postId').val());
				submit = true;
			}
			return submit;
		});

		/* Show how the post looks */
		$('#preview article header h2').html('<a href="#">' + $('input[name=title]').val() + '</a>');
		$('#preview article p').html($('textarea').val());

		$('input[name=title]').keyup(function() {
			$('#preview article header h2').html('<a href="#">' + $(this).val() + '</a>');
		})
		$('textarea').keyup(function() {
			$('#preview article p').html($(this).val());
		});

		/* Validations */
		$.validator.addMethod('defaultInput', function(value, element) {
			return this.optional(element) || (value !== '' && value !== 'Title of post' && value !== 'Tags');
		});
		$('form[name=post]').validate({
			errorPlacement: function() { },
			highlight: function(element, errorClass) {
				$(element).parent('li').addClass(errorClass);
			},
			unhighlight: function(element, errorClass) {
				$(element).parent('li').removeClass(errorClass);
			}
		});
	});

})(jQuery);