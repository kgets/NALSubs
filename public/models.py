from django.db import models
from djanbo.auth.models import AbstractUser

class User(AbstractUser):
	is_staff = models.BooleanField(default=False)
	is_franchisee = models.BooleanField(default=False)

class Upload(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	upload_date = models.DateTimeField('date uploaded')
	vis_staff = models.BooleanField(default=False)
	vis_franchisee = models.BooleanField(default=False)
	file = models.FileField(upload_to='/uploadedFiles/')

	def __str__(self):
		return self.title

