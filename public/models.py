from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class authType(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_sub_staff = models.BooleanField(default=False)
	is_sub_franchisee = models.BooleanField(default=False)
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		authType.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Upload(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	upload_date = models.DateTimeField('date uploaded')
	vis_staff = models.BooleanField(default=False)
	vis_franchisee = models.BooleanField(default=False)
	file = models.FileField(upload_to='uploadedFiles/')

	def __str__(self):
		return self.title
