from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from products import views

admin.site.site_header = 'Seamline Ghana ltd.'
admin.site.site_title = 'Seamline Ghana'
admin.site.index_title = 'Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.get_products)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

