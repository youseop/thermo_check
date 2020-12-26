from django.contrib import admin
from django.urls import path, include
import get_temp.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_temp.views.new, name='new'),
    # path('accounts/', include('accounts.urls')),
    path('get_temp/', include('get_temp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
