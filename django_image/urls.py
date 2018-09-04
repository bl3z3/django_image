from image import views
from image.sitemap import ThingSitemap, StaticSitemap, HomepageSitemap
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap

sitemaps = {
	"things": ThingSitemap,
	"static": StaticSitemap,
	"homepage": HomepageSitemap
}

urlpatterns = [
	url('index', views.index, name='home'),
	url(r'^things/(?P<slug>.+)/$', views.thing_detail, name='thing-details'),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
		name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	from django.conf import settings
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)