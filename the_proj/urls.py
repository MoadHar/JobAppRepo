
from django.contrib import admin
from django.urls import path, include

#mha
#from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('the_app.urls')),
    path('subscribe/', include('subscribe.urls')),
    path('upload/', include('upload_app.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
