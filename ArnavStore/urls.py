from django.contrib import admin
from django.urls import path
from ArnavStore.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),        # root URL
    path('index/', index)   # optional
]
