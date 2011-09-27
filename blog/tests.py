"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from blog.models import Post

class PostTests(TestCase):
	def test_add_tags(self):
		tags = 'a, b, c, d'
		post = Post.objects.create(title='test', message='test')
		post.add_tags(tags)
		self.assertEqual(post.tags.count(), 4)

		associated_tags = post.tags.all()
		self.assertEqual(associated_tags[0].name, 'a')
		self.assertEqual(associated_tags[3].name, 'd')
