from django.contrib import admin
from django.urls import path , include
from Products import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(urls))
]
