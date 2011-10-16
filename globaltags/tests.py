from django.test import TestCase
from blog.models import Post
from globaltags.templatetags import helper_tags

class TagsTest(TestCase):
	def test_title(self):
		title = helper_tags.title('/about/')
		self.assertEqual(title, 'about')
		title = helper_tags.title('/about/somethingelse/')
		self.assertEqual(title, 'about')
		title = helper_tags.title('')
		self.assertEqual(title, 'home')

		# Create a post and see if the title is the post title
		post = Post.objects.create(title='Dean is awesome', message='Dean is super awesome')
		title = helper_tags.title(post.uri())
		self.assertEqual(title, post.title)
		title = helper_tags.title('/blog/posts/')
		self.assertEqual(title, 'home')
