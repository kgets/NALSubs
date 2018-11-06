from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_cleanup.signals import cleanup_pre_delete

# class authType(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	is_sub_staff = models.BooleanField(default=False)
# 	is_sub_franchisee = models.BooleanField(default=False)
	
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		authType.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.authtype.save()

class Upload(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	upload_date = models.DateTimeField('date uploaded')
	vis_staff = models.BooleanField(default=False)
	vis_franchisee = models.BooleanField(default=False)
	file = models.FileField(upload_to='uploads/')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		try:
			this = Upload.objects.get(id=self.id)
			if this.file != self.file:
				this.file.delete(save=False)
		except: pass #with new file, do not delete old one
		super(Upload, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		try:
			this = Upload.objects.get(id=self.id)
			cleanup_pre_delete.connect()
		except: pass #with new file, do not delete old one
		super(Upload, self).delete(*args, **kwargs)
