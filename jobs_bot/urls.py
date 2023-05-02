from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path("jobs/", include("jobs.urls")),
    path("bot-users/", include("bot_users.urls")),
    path('admin/', admin.site.urls),
]
