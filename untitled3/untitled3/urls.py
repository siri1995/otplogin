from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from sample3.views import *
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)
router.register(r'address',AddressViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('sample3.urls')),
    url(r'^', include(router.urls))



]