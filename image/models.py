from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Timestamp(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
		ordering = ['created']

class Social(Timestamp):
	SOCIAL_TYPES = (
		('twitter', 'Twitter'),
		('facebook', 'Facebook'),
		('pinterest', 'Pinterest'),
		('instagram', 'Instagram'),
	)
	network = models.CharField(
		max_length=255, choices=SOCIAL_TYPES)
	username = models.CharField(max_length=255)
	thing = models.ForeignKey('Thing',
		related_name="social_accounts", on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Social Media Links"

class Thing(Timestamp):
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField()
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return "/things/%s/" % self.slug

	def __str__(self):
		return self.name

def get_image_path(instance, filename):
	return '/'.join(['thing_images', instance.thing.slug, filename])

class Upload(models.Model):
	thing = models.ForeignKey('Thing', related_name="uploads", on_delete=models.CASCADE)
	image = models.ImageField(upload_to=get_image_path)