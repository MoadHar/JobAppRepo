
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('the_app.urls')),
    path('subscribe/', include('subscribe.urls')),
]
