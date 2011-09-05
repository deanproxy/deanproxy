from django import forms
from blog.models import Comment, Post, Tag

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('tags',)