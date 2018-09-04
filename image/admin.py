from django.contrib import admin
from image.models import Social, Thing, Upload

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
	model = Social
	list_display = ('network', 'username')

class UploadAdmin(admin.ModelAdmin):
	list_display = ['thing']
	list_display_links = ['thing']

admin.site.register(Social, SocialAdmin)
admin.site.register(Thing)
admin.site.register(Upload, UploadAdmin)