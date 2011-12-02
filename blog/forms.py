from django import forms
from blog.models import Comment, Post, Tag

class CommentForm(forms.ModelForm):
	def is_valid(self):
		"""
		 We want to make sure we don't have spammers. They typically search for common fields
		 with common names. So our name field is something odd and we have a hidden field
		 with the common name in it. If that hidden field is altered, it's very probable that
		 we have a spammer and therefore validation should fail.
		"""
		is_good = False
		tackle = self.data['tackle'].strip()
		if self.data.get('name', '') != '':
			self._errors['name'] = self.error_class(['Spammers are not allowed'])
		if not tackle or tackle == 'Your name':
			self._errors['name'] = self.error_class(['Enter your name'])
		else:
			self.data['name'] = tackle
			is_good = True
			
		if is_good:
			is_good = super(CommentForm, self).is_valid()
		return is_good


	def save(self, commit=True):
		comment = super(CommentForm, self).save(commit=False)
		comment.name = self.data['tackle'].strip()
		if commit:
			comment.save()
		return comment

	class Meta:
		model = Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('tags',)