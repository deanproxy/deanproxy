from django.db import models

class Tweet(models.Model):
	created_at = models.DateField()
	text = models.CharField(max_length=140)

class Twitter(models.Model):
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=True, blank=True)

