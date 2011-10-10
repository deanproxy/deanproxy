(function($) {
	function appendComment(form) {
		$('#comments').append('<article id="newComment">' + form.message.value +
				'<footer>Posted by ' + form.tackle.value + ' less than a second ago</footer></article>');
		$('#newComment').effect('highlight', {}, 1000);
	}

	$(document).ready(function() {
		$('a[rel=delete]').click(function() {
			var that = this;
			var uri = $(this).attr('href');
			if (confirm('Are you sure you want to delete this?')) {
				$.get(uri, function() {
					/* If we deleted a comment, just remove it. Otherwise consider this a post deletion. */
					if (uri.match(/^\/blog\/comments\/delete\/\d+/)) {
						$(that).parent('footer').parent('article').fadeOut();
					} else {
						window.location.href = '/blog/posts/';
					}
				}).error(function() {
					alert('There was an error.');
				});
			}
			return false;
		});

		$('#comments article:even').addClass('even');

		$.validator.addMethod('validName', function(value, element) {
			return this.optional(element) || (value !== '' && value !== 'Your name');
		}, 'Must provide a valid name.');
		$('form[name=comment]').validate({
			submitHandler: function(form) {
				var li = $('#postComment').hide().parent('li');
				li.append('<span>Submitting <img src="/static/images/loading-pacman.gif"/></span>');
				$.post(form.action, $(form).serialize(), function() {
					li.html('Thanks for your input!');
					appendComment(form);
					return false;
				}).error(function() {
					alert('There was an issue when submitting this comment.');
					$('#postComment').show();
				}).complete(function() {
					$('#postComment').show();
					li.children('span').remove();
				});
				return false;
			},
			errorPlacement: function() {
				/* Don't do anything with error messages. */
			},
			highlight: function(element, errorClass) {
				$(element).parent('li').addClass(errorClass);
				$('#newCommentErrors').fadeIn();
			},
			unhighlight: function(element, errorClass) {
				$(element).parent('li').removeClass(errorClass);
				if ($('form ul li.error').length == 0) {
					$('#newCommentErrors').fadeOut();
				}
			}
		});

		/* Highlight javascript code */
		$('#posts article pre code').parent().addClass('prettyprint');
		prettyPrint();
	});
})(jQuery);