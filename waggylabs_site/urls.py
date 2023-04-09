from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views


DJANGO_ADMIN_BASE_URL =  getattr(settings, 'WAGGYLABS_DJANGO_ADMIN_BASE_URL', 'django-admin/')
WAGTAIL_ADMIN_BASE_URL =  getattr(settings, 'WAGGYLABS_WAGTAIL_ADMIN_BASE_URL', 'admin/')
WAGTAIL_DOCUMENTS_BASE_URL =  getattr(settings, 'WAGGYLABS_WAGTAIL_DOCUMENTS_BASE_URL', 'documents/')
CAPTCHA_BASE_URL = getattr(settings, 'WAGGYLABS_CAPTCHA_BASE_URL', 'captcha/')


urlpatterns = [
    path(DJANGO_ADMIN_BASE_URL, admin.site.urls),
    path(WAGTAIL_ADMIN_BASE_URL, include(wagtailadmin_urls)),
    path(WAGTAIL_DOCUMENTS_BASE_URL, include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    # according to django-simple-captcha docs
    path(CAPTCHA_BASE_URL, include('captcha.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
