from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls


from waggylabs import views as search_views


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