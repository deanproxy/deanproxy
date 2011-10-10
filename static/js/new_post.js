(function($) {

	function setAtCurrentPosition(textarea, text) {
		var caretStart = textarea.get(0).selectionStart;
		var caretEnd = textarea.get(0).selectionEnd;
		var markdown = textarea.val().substr(0, caretStart) + text +
			textarea.val().substr(caretEnd, textarea.val().length);
		textarea.val(markdown);
		textarea.get(0).selectionStart = caretStart + 1;
		textarea.get(0).selectionEnd = caretStart + 15;
	}


	$(document).ready(function() {
		$('#delete').click(function() {
			var submit = false;
			if (confirm('Really delete this post?')) {
				$('form').attr('action', '/blog/posts/delete/' + $('#postId').val());
				submit = true;
			}
			return submit;
		});

		/* Show how the post looks */
		var converter = new Attacklab.showdown.converter();

		$('#preview article header h2').html('<a href="#">' + $('input[name=title]').val() + '</a>');
		$('#preview article p').html(converter.makeHtml($('textarea').val()));

		$('input[name=title]').keyup(function() {
			$('#preview article header h2').html('<a href="#">' + $(this).val() + '</a>');
		})
		$('textarea').keyup(function() {
			$('#preview article p').html(converter.makeHtml($(this).val()));
		});
		setInterval(function() {
			$('#preview article p').find('pre code').parent().addClass('prettyprint');
			prettyPrint();
		}, 20000);

		/* Validations */
		$.validator.addMethod('defaultInput', function(value, element) {
			return this.optional(element) || (value !== '' && value !== 'Title of post' && value !== 'Tags');
		});
		$('form[name=post]').validate({
			wrapper: 'span',
			rules: {
				title: {
					minlength: 5,
					maxlength: 100
				}
			},
			errorPlacement: function(error, element) {
				if (element.attr('name') != 'message') {
					error.appendTo(element.parent('li'));
				}
			},
			highlight: function(element, errorClass) {
				$(element).parent('li').addClass(errorClass);
			},
			unhighlight: function(element, errorClass) {
				$(element).parent('li').removeClass(errorClass);
			}
		});

		$('.postHelpers .img').click(function() {

		});

		$('.postHelpers .href').click(function() {
			var link = prompt('Enter the link');
			if (link) {
				var textarea = $('textarea[name=message]');
				setAtCurrentPosition(textarea, "[url description](" + link + ") ");
			}
		});
	});

})(jQuery);