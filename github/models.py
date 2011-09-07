from django.db import models

class Commit(models.Model):
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
	committed_date = models.DateTimeField()
	message = models.CharField(max_length=250)
	committer = models.CharField(max_length=250)
	project = models.CharField(max_length=50, primary_key=True)


