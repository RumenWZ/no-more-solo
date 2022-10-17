from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NoSolo.main.urls')),
    path('accounts/', include('NoSolo.accounts.urls')),
]
