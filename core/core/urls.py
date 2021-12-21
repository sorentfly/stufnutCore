from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='core.home'),
    path('admin/', admin.site.urls),
    path('base/', include('base.urls')),
]
