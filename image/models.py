from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Social(models.Model):
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

class Thing(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField()
	user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return "/things/%s/" % self.slug