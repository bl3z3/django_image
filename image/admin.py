from django.contrib import admin
from image.models import Social, Thing

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
	model = Social
	list_display = ('network', 'username')

admin.site.register(Social, SocialAdmin)
admin.site.register(Thing)