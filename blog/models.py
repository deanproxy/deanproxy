from django.db import models
import re

class Tag(models.Model):
	name = models.CharField(max_length=50, primary_key=True, unique=True)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100)
	message = models.TextField()
	tags = models.ManyToManyField('Tag')

	def uri(self):
		title = re.sub('[!@#\$%\^&\*\(\),<>\\\\{}\|\s\[\]\.]', '-', self.title.lower())
		return "/blog/posts/%d/%s/%d-%s.html" % (self.created_at.year, self.created_at.strftime("%m"), self.id, title)


	# tag_str: 'some, tags, delimited, by, commas'
	# Parses the tag_str and assigns the tags to the post as long as they're not already
	# assigned to the post. If the tag does not exist, it creates it.
	def add_tags(self, tag_str):
		tags = self.tags.all()
		tag_strings = [t.strip() for t in tag_str.split(',')]
		for tag_name in set(tag_strings):
			try:
				tag = Tag.objects.get(pk=tag_name)
			except Tag.DoesNotExist:
				tag = Tag.objects.create(name=tag_name)
			if tag not in tags:
				self.tags.add(tag)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=30)
	message = models.TextField()


