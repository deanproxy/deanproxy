from django.db import models
import re
import markdown2

class Tag(models.Model):
	name = models.CharField(max_length=50, primary_key=True, unique=True)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100, blank=False)
	message = models.TextField()
	html_message = models.TextField(blank=True)
	tags = models.ManyToManyField('Tag')

	def save(self, force_insert=False, force_update=False, using=None):
		"""
		 parse the markdown into html.
		"""
		self.html_message = markdown2.markdown(self.message)
		super(Post, self).save(force_insert, force_update, using)

	def uri(self):
		title = re.sub('[!:;@#\$%\^&\*\(\),<>\\\\{}\|\s\[\]\.\']', '-', self.title.lower())
		return "/blog/posts/%d/%s/%d-%s.html" % (self.created_at.year, self.created_at.strftime("%m"), self.id, title)

	def next(self):
		post = Post.objects.filter(created_at__gt=self.created_at).order_by('created_at')
		if post:
			post = post[0]
		return post

	def prev(self):
		post = Post.objects.filter(created_at__lt=self.created_at).order_by('created_at').reverse()
		if post:
			post = post[0]
		return post

	def add_tags(self, tag_str):
		"""
		 tag_str: 'some, tags, delimited, by, commas'
		 Parses the tag_str and assigns the tags to the post as long as they're not already
		 assigned to the post. If the tag does not exist, it creates it.
		"""
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
	is_admin = models.BooleanField(default=False, blank=True)

	def save(self, force_insert=False, force_update=False, using=None):
		' Make sure no HTML is here and also remove some markdown that is not allowed '

		safe_message = re.sub(r'!\[["\'!\.&*#@%\^\-=\{}:/\w\s]*]\([\.:/\w\s]*(?:\s["\'\.!&*#@%\^\-=\{}:/\w\s]*)?\)',
							  '_[img-removed]_', self.message)
		self.message = markdown2.markdown(safe_message, safe_mode='escape')
		super(Comment, self).save(force_insert=force_insert, force_update=force_update, using=using)




