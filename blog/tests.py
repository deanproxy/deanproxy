"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import simplejson
from blog.models import Post
from blog.models import Comment
from django.test.client import Client

class PostTests(TestCase):
	client = Client()

	def test_add_tags(self):
		tags = 'a, b, c, d'
		post = Post.objects.create(title='test', message='test')
		post.add_tags(tags)
		self.assertEqual(post.tags.count(), 4)

		associated_tags = post.tags.all()
		self.assertEqual(associated_tags[0].name, 'a')
		self.assertEqual(associated_tags[3].name, 'd')

	def test_add_comment(self):
		post = Post.objects.create(title='Test', message='test')
		response = self.client.post('/blog/comments/create/', {'post':post.id, 'name':'Stupid Spammers', 'tackle':'Dean', 'message':'Hello, Mr. Ed'})
		self.assertEqual(response['Content-Type'], 'application/json')
		json = simplejson.loads(response.content)
		self.assertEqual(json['name'], 'Dean')
		self.assertEqual(json['message'], '<p>Hello, Mr. Ed</p>\n')


	def test_save_comment(self):
		markdown = """This is going to be markdown.

![Image stuff](http://deanproxy.com/images/stuff.jpg "Ha!")

That image should be removed
        """
		markup = """<p>This is going to be markdown.</p>

<p><em>[img-removed]</em></p>

<p>That image should be removed</p>
"""
		post = Post.objects.create(title='Test', message='Bob')
		comment = Comment.objects.create(post=post, name='Dean', message=markdown)
		self.assertEqual(comment.name, "Dean")
		self.assertEqual(comment.message, markup)

