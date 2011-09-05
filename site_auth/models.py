from django.db import models
import hashlib

class Admin(models.Model):
	SALT = '$@67faltme'

	username = models.CharField(max_length=30)
	password = models.CharField(max_length=128)

	@staticmethod
	def authenticate(username, password):
		user = None
		try:
			user = Admin.objects.get(username=username)
		except Admin.DoesNotExist:
			raise
		else:
			if not user.check_password(password):
				raise Admin.PermissionDenied
		return user

	@staticmethod
	def make_password(raw_password):
		return hashlib.sha1(Admin.SALT + raw_password).hexdigest()

	@staticmethod
	def create_user(username, password):
		real_password = Admin.make_password(password)
		return Admin.objects.create(username=username, password=real_password)

	def check_password(self, raw_password):
		hash = Admin.make_password(raw_password)
		return hash == self.password




