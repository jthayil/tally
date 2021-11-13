from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    url("rest-auth/", include("rest_auth.urls")),
    url("rest-auth/registration/", include("rest_auth.registration.urls")),
    url("", include("tally.urls")),
]
